
from pydantic import Field, validator
from typing import List, Optional, Union, Literal
from sdks.novavision.src.base.model import Package, Image, Inputs, Configs, Outputs, Response, Request, Output, Input, Config, KeyPoints as BaseKeyPoints, Detection as BaseDetection


class InputImage(Input):
    name: Literal["inputImage"] = "inputImage"
    value: Union[Image, List[Image]]
    type: Literal["object"] = "object"

    class Config:
        title = "Image"

class KeyPoints(BaseKeyPoints):
    size: float | None = None
    angle: float | None = None
    response: float | None = None
    octave: int | None = None
    class_id: int | None = None

class Detection(BaseDetection):
    keyPoints: Optional[List[KeyPoints]] = None

class OutputDetections(Output):
    name: Literal["outputDetections"] = "outputDetections"
    value: List[Detection]
    type: Literal["list"] = "list"

    class Config:
        title = "Output Detections"


class OutputData(Output):
    name: Literal["outputData"] = "outputData"
    value: Union[list, dict]
    type: Literal["object"] = "object"

    class Config:
        title = "Output Data"

class OutputImage(Output):
    name: Literal["outputImage"] = "outputImage"
    value: Image
    type: Literal["object"] = "object"

    class Config:
        title = "Output Image"


class SiftInputs(Inputs):
    inputImage: InputImage

class MaxFeaturesValue(Config):
    name: Literal["maxFeatures"] = "maxFeatures"
    value: int = Field(default=0, ge=0, le=100000)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Max Features"
        json_schema_extra = {"shortDescription": "OpenCV SIFT nfeatures (0 = unlimited)"}


class MaxFeaturesEnableOn(Config):
    name: Literal["maxFeaturesEnableOn"] = "maxFeaturesEnableOn"
    value: Literal[True] = True
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    maxFeatures: MaxFeaturesValue

    class Config:
        title = "Enabled"
        json_schema_extra = {"target": "maxFeatures"}


class MaxFeaturesEnableOff(Config):
    name: Literal["maxFeaturesEnableOff"] = "maxFeaturesEnableOff"
    value: Literal[False] = False
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    class Config:
        title = "Disabled"


class ConfigMaxFeatures(Config):
    """
    Enable/disable user override for SIFT nfeatures.
    """
    name: Literal["configMaxFeatures"] = "configMaxFeatures"
    value: Union[MaxFeaturesEnableOn, MaxFeaturesEnableOff]
    type: Literal["object"] = "object"
    field: Literal["dropdownlist"] = "dropdownlist"

    class Config:
        title = "Max Features"
        json_schema_extra = {"shortDescription": "Enable and set maximum number of SIFT keypoints"}


class ContrastThresholdValue(Config):
    name: Literal["contrastThreshold"] = "contrastThreshold"
    value: float = Field(default=0.04, ge=0.001, le=0.2)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Contrast Threshold"
        json_schema_extra = {"shortDescription": "OpenCV SIFT contrastThreshold"}


class ContrastEnableOn(Config):
    name: Literal["contrastEnableOn"] = "contrastEnableOn"
    value: Literal[True] = True
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    contrastThreshold: ContrastThresholdValue

    class Config:
        title = "Enabled"
        json_schema_extra = {"target": "contrastThreshold"}


class ContrastEnableOff(Config):
    name: Literal["contrastEnableOff"] = "contrastEnableOff"
    value: Literal[False] = False
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    class Config:
        title = "Disabled"


class ConfigContrastThreshold(Config):
    name: Literal["configContrastThreshold"] = "configContrastThreshold"
    value: Union[ContrastEnableOn, ContrastEnableOff]
    type: Literal["object"] = "object"
    field: Literal["dropdownlist"] = "dropdownlist"

    class Config:
        title = "Contrast Threshold"
        json_schema_extra = {"shortDescription": "Enable and set SIFT contrastThreshold"}


class EdgeThresholdValue(Config):
    name: Literal["edgeThreshold"] = "edgeThreshold"
    value: float = Field(default=10, ge=1, le=100)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Edge Threshold"
        json_schema_extra = {"shortDescription": "OpenCV SIFT edgeThreshold"}


class EdgeEnableOn(Config):
    name: Literal["edgeEnableOn"] = "edgeEnableOn"
    value: Literal[True] = True
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    edgeThreshold: EdgeThresholdValue

    class Config:
        title = "Enabled"
        json_schema_extra = {"target": "edgeThreshold"}


class EdgeEnableOff(Config):
    name: Literal["edgeEnableOff"] = "edgeEnableOff"
    value: Literal[False] = False
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    class Config:
        title = "Disabled"


class ConfigEdgeThreshold(Config):
    name: Literal["configEdgeThreshold"] = "configEdgeThreshold"
    value: Union[EdgeEnableOn, EdgeEnableOff]
    type: Literal["object"] = "object"
    field: Literal["dropdownlist"] = "dropdownlist"

    class Config:
        title = "Edge Threshold"
        json_schema_extra = {"shortDescription": "Enable and set SIFT edgeThreshold"}


class SigmaValue(Config):
    name: Literal["sigma"] = "sigma"
    value: float = Field(default=1.6, ge=0.1, le=10.0)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Sigma"
        json_schema_extra = {"shortDescription": "OpenCV SIFT sigma"}


class SigmaEnableOn(Config):
    name: Literal["sigmaEnableOn"] = "sigmaEnableOn"
    value: Literal[True] = True
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    sigma: SigmaValue

    class Config:
        title = "Enabled"
        json_schema_extra = {"target": "sigma"}


class SigmaEnableOff(Config):
    name: Literal["sigmaEnableOff"] = "sigmaEnableOff"
    value: Literal[False] = False
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    class Config:
        title = "Disabled"


class ConfigSigma(Config):
    name: Literal["configSigma"] = "configSigma"
    value: Union[SigmaEnableOn, SigmaEnableOff]
    type: Literal["object"] = "object"
    field: Literal["dropdownlist"] = "dropdownlist"

    class Config:
        title = "Sigma"
        json_schema_extra = {"shortDescription": "Enable and set SIFT sigma"}


class OctaveLayersValue(Config):
    name: Literal["nOctaveLayers"] = "nOctaveLayers"
    value: int = Field(default=3, ge=1, le=10)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Octave Layers"
        json_schema_extra = {"shortDescription": "OpenCV SIFT nOctaveLayers"}


class OctaveLayersEnableOn(Config):
    name: Literal["octaveLayersEnableOn"] = "octaveLayersEnableOn"
    value: Literal[True] = True
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    nOctaveLayers: OctaveLayersValue

    class Config:
        title = "Enabled"
        json_schema_extra = {"target": "nOctaveLayers"}


class OctaveLayersEnableOff(Config):
    name: Literal["octaveLayersEnableOff"] = "octaveLayersEnableOff"
    value: Literal[False] = False
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    class Config:
        title = "Disabled"


class ConfigOctaveLayers(Config):
    name: Literal["configOctaveLayers"] = "configOctaveLayers"
    value: Union[OctaveLayersEnableOn, OctaveLayersEnableOff]
    type: Literal["object"] = "object"
    field: Literal["dropdownlist"] = "dropdownlist"

    class Config:
        title = "Octave Layers"
        json_schema_extra = {"shortDescription": "Enable and set SIFT nOctaveLayers"}


class SiftConfigs(Configs):
    configMaxFeatures: ConfigMaxFeatures
    configContrastThreshold: ConfigContrastThreshold
    configEdgeThreshold: ConfigEdgeThreshold
    configSigma: ConfigSigma
    configOctaveLayers: ConfigOctaveLayers

class SiftOutputs(Outputs):
    outputImage: OutputImage
    outputData: OutputData
    outputDetections: OutputDetections


class SiftRequest(Request):
    inputs: Optional[SiftInputs]
    configs: SiftConfigs

    class Config:
        json_schema_extra = {
            "target": "configs"
        }


class SiftResponse(Response):
    outputs: SiftOutputs


class SiftExecutor(Config):
    name: Literal["Sift"] = "Sift"
    value: Union[SiftRequest, SiftResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "Sift"
        json_schema_extra = {

            "target": {
                "value": 0
            }
        }


class ConfigExecutor(Config):
    name: Literal["ConfigExecutor"] = "ConfigExecutor"
    value: Union[SiftExecutor]
    type: Literal["executor"] = "executor"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Task"
        json_schema_extra = {
            "target": "value"
        }


class PackageConfigs(Configs):
    executor: ConfigExecutor


class PackageModel(Package):
    configs: PackageConfigs
    type: Literal["component"] = "component"
    name: Literal["Sift"] = "Sift"