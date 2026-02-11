
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
    descriptor: Optional[List[float]] = None

class Detection(BaseDetection):
    keyPoints: Optional[List[KeyPoints]] = None

class OutputDetections(Output):
    name: Literal["outputDetections"] = "outputDetections"
    value: List[Detection]
    type: Literal["list"] = "list"

    class Config:
        title = "Output Detections"


class OutputImage(Output):
    name: Literal["outputImage"] = "outputImage"
    value: Image
    type: Literal["object"] = "object"

    class Config:
        title = "Output Image"


class SiftInputs(Inputs):
    inputImage: InputImage


class ConfigMaxFeaturesValue(Config):
    name: Literal["configMaxFeaturesValue"] = "configMaxFeaturesValue"
    value: int = Field(default=0, ge=0, le=100000)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Max Features"


class MaxFeaturesEnabled(Config):
    name: Literal["MaxFeaturesEnabled"] = "MaxFeaturesEnabled"
    value: Literal["MaxFeaturesEnabled"] = "MaxFeaturesEnabled"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"
    configMaxFeaturesValue: ConfigMaxFeaturesValue

    class Config:
        title = "Enabled"


class MaxFeaturesDisabled(Config):
    name: Literal["MaxFeaturesDisabled"] = "MaxFeaturesDisabled"
    value: int = 0
    type: Literal["number"] = "number"
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


class ConfigContrastThresholdValue(Config):
    name: Literal["configContrastThresholdValue"] = "configContrastThresholdValue"
    value: float = Field(default=0.04, ge=0.001, le=0.2)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Contrast Threshold"


class ContrastThresholdEnabled(Config):
    name: Literal["ContrastThresholdEnabled"] = "ContrastThresholdEnabled"
    value: Literal["ContrastThresholdEnabled"] = "ContrastThresholdEnabled"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"
    configContrastThresholdValue: ConfigContrastThresholdValue

    class Config:
        title = "Enabled"


class ContrastThresholdDisabled(Config):
    name: Literal["ContrastThresholdDisabled"] = "ContrastThresholdDisabled"
    value: float = 0.04
    type: Literal["number"] = "number"
    field: Literal["option"] = "option"

    class Config:
        title = "Disabled"


class ConfigContrastThreshold(Config):
    name: Literal["configContrastThreshold"] = "configContrastThreshold"
    value: Union[ContrastThresholdEnabled, ContrastThresholdDisabled]
    type: Literal["object"] = "object"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Contrast Threshold"


class ConfigEdgeThresholdValue(Config):
    name: Literal["configEdgeThresholdValue"] = "configEdgeThresholdValue"
    value: float = Field(default=10, ge=1, le=100)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Edge Threshold"


class EdgeThresholdEnabled(Config):
    name: Literal["EdgeThresholdEnabled"] = "EdgeThresholdEnabled"
    value: Literal["EdgeThresholdEnabled"] = "EdgeThresholdEnabled"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"
    configEdgeThresholdValue: ConfigEdgeThresholdValue

    class Config:
        title = "Enabled"


class EdgeThresholdDisabled(Config):
    name: Literal["EdgeThresholdDisabled"] = "EdgeThresholdDisabled"
    value: float = 10.0
    type: Literal["number"] = "number"
    field: Literal["option"] = "option"

    class Config:
        title = "Disabled"


class ConfigEdgeThreshold(Config):
    name: Literal["configEdgeThreshold"] = "configEdgeThreshold"
    value: Union[EdgeThresholdEnabled, EdgeThresholdDisabled]
    type: Literal["object"] = "object"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Edge Threshold"

class ConfigSigmaValue(Config):
    name: Literal["configSigmaValue"] = "configSigmaValue"
    value: float = Field(default=1.6, ge=0.1, le=10.0)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Sigma"


class SigmaEnabled(Config):
    name: Literal["SigmaEnabled"] = "SigmaEnabled"
    value: Literal["SigmaEnabled"] = "SigmaEnabled"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"
    configSigmaValue: ConfigSigmaValue

    class Config:
        title = "Enabled"


class SigmaDisabled(Config):
    name: Literal["SigmaDisabled"] = "SigmaDisabled"
    value: float = 1.6
    type: Literal["number"] = "number"
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


class ConfigOctaveLayersValue(Config):
    name: Literal["configOctaveLayersValue"] = "configOctaveLayersValue"
    value: int = Field(default=3, ge=1, le=10)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Octave Layers"


class OctaveLayersEnabled(Config):
    name: Literal["OctaveLayersEnabled"] = "OctaveLayersEnabled"
    value: Literal["OctaveLayersEnabled"] = "OctaveLayersEnabled"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"
    configOctaveLayersValue: ConfigOctaveLayersValue

    class Config:
        title = "Enabled"


class OctaveLayersDisabled(Config):
    name: Literal["OctaveLayersDisabled"] = "OctaveLayersDisabled"
    value: int = 3
    type: Literal["number"] = "number"
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

class SiftConfigs(Configs):
    configMaxFeatures: ConfigMaxFeatures
    configContrastThreshold: ConfigContrastThreshold
    configEdgeThreshold: ConfigEdgeThreshold
    configSigma: ConfigSigma
    configOctaveLayers: ConfigOctaveLayers

class SiftOutputs(Outputs):
    outputImage: OutputImage
    outputDetections: OutputDetections


class SiftRequest(Request):
    inputs: Optional[SiftInputs] = None
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