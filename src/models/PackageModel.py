
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

class MaxFeaturesEnabled(Config):
    name: Literal["Enabled"] = "Enabled"
    value: MaxFeaturesValue                 # ✅ textbox config burada
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "Enabled"
        json_schema_extra = {"target": "value"}

class MaxFeaturesDisabled(Config):
    name: Literal["Disabled"] = "Disabled"
    value: Literal[False] = False
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    class Config:
        title = "Disabled"

class ConfigMaxFeatures(Config):
    name: Literal["configMaxFeatures"] = "configMaxFeatures"
    value: Union[MaxFeaturesEnabled, MaxFeaturesDisabled]
    type: Literal["object"] = "object"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Max Features"
        json_schema_extra = {"shortDescription": "Enable and set maximum number of SIFT keypoints", "target": "value"}


class ContrastThresholdValue(Config):
    name: Literal["contrastThreshold"] = "contrastThreshold"
    value: float = Field(default=0.04, ge=0.001, le=0.2)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Contrast Threshold"
        json_schema_extra = {"shortDescription": "OpenCV SIFT contrastThreshold"}

class ContrastEnabled(Config):
    name: Literal["Enabled"] = "Enabled"
    value: ContrastThresholdValue
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "Enabled"
        json_schema_extra = {"target": "value"}

class ContrastDisabled(Config):
    name: Literal["Disabled"] = "Disabled"
    value: Literal[False] = False
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    class Config:
        title = "Disabled"

class ConfigContrastThreshold(Config):
    name: Literal["configContrastThreshold"] = "configContrastThreshold"
    value: Union[ContrastEnabled, ContrastDisabled]
    type: Literal["object"] = "object"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Contrast Threshold"
        json_schema_extra = {"shortDescription": "Enable and set SIFT contrastThreshold", "target": "value"}


class EdgeThresholdValue(Config):
    name: Literal["edgeThreshold"] = "edgeThreshold"
    value: float = Field(default=10, ge=1, le=100)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Edge Threshold"
        json_schema_extra = {"shortDescription": "OpenCV SIFT edgeThreshold"}

class EdgeEnabled(Config):
    name: Literal["Enabled"] = "Enabled"
    value: EdgeThresholdValue
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "Enabled"
        json_schema_extra = {"target": "value"}

class EdgeDisabled(Config):
    name: Literal["Disabled"] = "Disabled"
    value: Literal[False] = False
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    class Config:
        title = "Disabled"

class ConfigEdgeThreshold(Config):
    name: Literal["configEdgeThreshold"] = "configEdgeThreshold"
    value: Union[EdgeEnabled, EdgeDisabled]
    type: Literal["object"] = "object"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Edge Threshold"
        json_schema_extra = {"shortDescription": "Enable and set SIFT edgeThreshold", "target": "value"}


class SigmaValue(Config):
    name: Literal["sigma"] = "sigma"
    value: float = Field(default=1.6, ge=0.1, le=10.0)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Sigma"
        json_schema_extra = {"shortDescription": "OpenCV SIFT sigma"}

class SigmaEnabled(Config):
    name: Literal["Enabled"] = "Enabled"
    value: SigmaValue
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "Enabled"
        json_schema_extra = {"target": "value"}

class SigmaDisabled(Config):
    name: Literal["Disabled"] = "Disabled"
    value: Literal[False] = False
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    class Config:
        title = "Disabled"

class ConfigSigma(Config):
    name: Literal["configSigma"] = "configSigma"
    value: Union[SigmaEnabled, SigmaDisabled]
    type: Literal["object"] = "object"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Sigma"
        json_schema_extra = {"shortDescription": "Enable and set SIFT sigma", "target": "value"}


class OctaveLayersValue(Config):
    name: Literal["nOctaveLayers"] = "nOctaveLayers"
    value: int = Field(default=3, ge=1, le=10)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Octave Layers"
        json_schema_extra = {"shortDescription": "OpenCV SIFT nOctaveLayers"}

class OctaveLayersEnabled(Config):
    name: Literal["Enabled"] = "Enabled"
    value: OctaveLayersValue
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "Enabled"
        json_schema_extra = {"target": "value"}

class OctaveLayersDisabled(Config):
    name: Literal["Disabled"] = "Disabled"
    value: Literal[False] = False
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    class Config:
        title = "Disabled"

class ConfigOctaveLayers(Config):
    name: Literal["configOctaveLayers"] = "configOctaveLayers"
    value: Union[OctaveLayersEnabled, OctaveLayersDisabled]
    type: Literal["object"] = "object"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Octave Layers"
        json_schema_extra = {"shortDescription": "Enable and set SIFT nOctaveLayers", "target": "value"}

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