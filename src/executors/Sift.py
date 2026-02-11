import os
import sys
import cv2
import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../../"))

from sdks.novavision.src.media.image import Image
from sdks.novavision.src.base.component import Component
from sdks.novavision.src.helper.executor import Executor
from components.Sift.src.utils.response import build_response
from components.Sift.src.models.PackageModel import PackageModel
from sdks.novavision.src.base.model import Image as ImageModel


class Sift(Component):
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        self.request.model = PackageModel(**self.request.data)

        self.image = self.request.get_param("inputImage")
        self.max_features = self.request.get_param("configMaxFeaturesValue")
        self.contrast = self.request.get_param("configContrastThresholdValue")
        self.edge = self.request.get_param("configEdgeThresholdValue")
        self.sigma = self.request.get_param("configSigmaValue")
        self.octave_layers = self.request.get_param("configOctaveLayersValue")
        self.outputData = {}

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    @staticmethod
    def _ensure_uint8(arr: np.ndarray) -> np.ndarray:
        return arr.astype(np.uint8) if arr.dtype != np.uint8 else arr

    def sift_inference(self):
        img = Image.get_frame(img=self.image, redis_db=self.redis_db)
        frame = self._ensure_uint8(np.asarray(img.value))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        nfeatures = int(self.max_features) if self.max_features is not None else 0
        contrast = float(self.contrast) if self.contrast is not None else 0.04
        edge = float(self.edge) if self.edge is not None else 10.0
        sigma = float(self.sigma) if self.sigma is not None else 1.6
        octave_layers = int(self.octave_layers) if self.octave_layers is not None else 3

        sift = cv2.SIFT_create(
            nfeatures=nfeatures,
            nOctaveLayers=octave_layers,
            contrastThreshold=contrast,
            edgeThreshold=edge,
            sigma=sigma,
        )

        kp, des = sift.detectAndCompute(gray, None)
        kp = kp or []
        if des is None:
            des = np.zeros((0, 128), dtype=np.float32)
        else:
            des = np.asarray(des, dtype=np.float32)

        vis = cv2.drawKeypoints(frame, kp, None)

        keypoints_payload = []
        for p in kp:
            keypoints_payload.append(
                {
                    "cx": float(p.pt[0]),
                    "cy": float(p.pt[1]),
                    "size": float(p.size),
                    "angle": float(p.angle),
                    "response": float(p.response),
                    "octave": int(p.octave),
                }
            )

        self.outputData = {
            "descriptors": {
                "shape": [int(des.shape[0]), int(des.shape[1])],
                "dtype": "float32",
                "values": des.tolist(),
            },
            "keypoints": keypoints_payload,
        }
        out_img = ImageModel(
            name=img.name,
            uID=img.uID,
            mimeType=img.mimeType,
            encoding=img.encoding,
            value=vis,
            type=img.type,
        )
        self.image = Image.set_frame(img=out_img, package_uID=self.uID, redis_db=self.redis_db)

        return build_response(context=self)

    def run(self):
        return self.sift_inference()

if "__main__" == __name__:
    Executor(sys.argv[1]).run()
