
from sdks.novavision.src.helper.package import PackageHelper
from components.Sift.src.models.PackageModel import PackageModel, PackageConfigs, ConfigExecutor, SiftOutputs, SiftResponse, SiftExecutor, OutputImage, OutputDetections


def build_response(context):
    outputDetections = OutputDetections(value=context.detections)
    siftOutputs = SiftOutputs(outputDetections=outputDetections)
    siftResponse = SiftResponse(outputs=siftOutputs)
    siftExecutor = SiftExecutor(value=siftResponse)
    executor = ConfigExecutor(value=siftExecutor)
    packageConfigs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel