
from sdks.novavision.src.helper.package import PackageHelper
from components.Sift.src.models.PackageModel import PackageModel, PackageConfigs, ConfigExecutor, SiftOutputs, SiftResponse, SiftExecutor, OutputImage, OutputData


def build_response(context):
    outputData = OutputData(value=context.outputData)
    outputImage = OutputImage(value=context.image)
    siftOutputs = SiftOutputs(outputImage=outputImage, outputData=outputData)
    siftResponse = SiftResponse(outputs=siftOutputs)
    siftExecutor = SiftExecutor(value=siftResponse)
    executor = ConfigExecutor(value=siftExecutor)
    packageConfigs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel