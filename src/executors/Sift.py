"""
    It is one of the preprocessing components in which the image is rotated.
"""

import os
import cv2
import sys
import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))

from sdks.novavision.src.media.image import Image
from sdks.novavision.src.base.component import Component
from sdks.novavision.src.helper.executor import Executor
from components.Sift.src.utils.response import build_response
from components.Sift.src.models.PackageModel import PackageModel, Keypoints, Detection
from sdks.novavision.src.base.model import KeyPoints
from sdks.novavision.src.base.model import Image as ImageModel

class Sift(Component):
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        self.request.model = PackageModel(**(self.request.data))
        self.image = self.request.get_param("inputImage")
        self.cfg_max_features = self.request.get_param("configMaxFeatures")
        self.cfg_contrast = self.request.get_param("configContrastThreshold")
        self.cfg_edge = self.request.get_param("configEdgeThreshold")
        self.cfg_sigma = self.request.get_param("configSigma")
        self.cfg_octave = self.request.get_param("configOctaveLayers")

        self.detections = []
        self.outputData = {}

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    @staticmethod
    def _ensure_uint8(img: np.ndarray) -> np.ndarray:
        if img.dtype != np.uint8:
            img = img.astype(np.uint8)
        return img

    @staticmethod
    def _kp_to_model(kp) -> KeyPoints:
        return KeyPoints(
            cx=float(kp.pt[0]),
            cy=float(kp.pt[1]),
            size=float(kp.size),
            angle=float(kp.angle),
            response=float(kp.response),
            octave=int(kp.octave),
            class_id=int(kp.class_id),
        )

    @staticmethod
    def _is_disabled(cfg) -> bool:
        return cfg.value.value is False

    def sift_inference(self):
        img = Image.get_frame(img=self.image, redis_db=self.redis_db)
        frame = self._ensure_uint8(np.asarray(img.value))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        nfeatures = (
            self.cfg_max_features.value.configMaxFeaturesValue.value
            if not self._is_disabled(self.cfg_max_features)
            else 0
        )

        contrast = (
            self.cfg_contrast.value.configContrastThresholdValue.value
            if not self._is_disabled(self.cfg_contrast)
            else 0.04
        )

        edge = (
            self.cfg_edge.value.configEdgeThresholdValue.value
            if not self._is_disabled(self.cfg_edge)
            else 10
        )

        sigma = (
            self.cfg_sigma.value.configSigmaValue.value
            if not self._is_disabled(self.cfg_sigma)
            else 1.6
        )

        octave_layers = (
            self.cfg_octave.value.configOctaveLayersValue.value
            if not self._is_disabled(self.cfg_octave)
            else 3
        )

        sift = cv2.SIFT_create(
            nfeatures=int(nfeatures),
            nOctaveLayers=int(octave_layers),
            contrastThreshold=float(contrast),
            edgeThreshold=float(edge),
            sigma=float(sigma),
        )

        kp, des = sift.detectAndCompute(gray, None)

        if kp is None:
            kp = []
        if des is None:
            des = np.zeros((0, 128), dtype=np.float32)
        else:
            des = np.asarray(des, dtype=np.float32)

        vis = cv2.drawKeypoints(frame, kp, None)

        keypoints_model = [self._kp_to_model(p) for p in kp]

        self.detections = [
            Detection(
                confidence=1.0,
                classId=0,
                classLabel="SIFT",
                keyPoints=keypoints_model,
                boundingBox=None,
            )
        ]

        self.outputData = {
            "descriptors": {
                "shape": [int(des.shape[0]), int(des.shape[1])],
                "dtype": "float32",
                "values": des.tolist(),
            }
        }

        out_img = ImageModel(
            name=img.name,
            uID=img.uID,
            mimeType=img.mimeType,
            encoding=img.encoding,
            value=vis,
            type=img.type,
        )

        self.image = Image.set_frame(
            img=out_img,
            package_uID=self.uID,
            redis_db=self.redis_db,
        )

        return build_response(context=self)

    def run(self):
        return self.sift_inference()

if "__main__" == __name__:
    Executor(sys.argv[1]).run()