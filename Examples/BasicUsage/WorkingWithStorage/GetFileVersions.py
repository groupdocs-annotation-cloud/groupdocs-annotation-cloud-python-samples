# Import modules
import groupdocs_annotation_cloud

from Common import Common

class GetFileVersions:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_annotation_cloud.StorageApi.from_config(Common.GetConfig())
        
        try:
            request = groupdocs_annotation_cloud.GetFileVersionsRequest("annotationdocs\\one-page.docx", Common.myStorage)
            response = api.get_file_versions(request)
            
            print("Expected response type is FileVersions: " + str(response))
        except groupdocs_annotation_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))