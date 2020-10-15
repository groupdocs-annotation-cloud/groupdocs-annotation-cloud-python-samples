import groupdocs_annotation_cloud

from Common import Common

class GetSupportedFormats:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_annotation_cloud.InfoApi.from_config(Common.GetConfig())
        result = api.get_supported_file_formats()
        print("Formats count: " + str(len(result.formats)))
