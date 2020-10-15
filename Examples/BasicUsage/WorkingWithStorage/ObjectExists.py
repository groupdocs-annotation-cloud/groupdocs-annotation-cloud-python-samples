# Import modules
import groupdocs_annotation_cloud

from Common import Common

class ObjectExists:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_annotation_cloud.StorageApi.from_config(Common.GetConfig())
        
        try:
            request = groupdocs_annotation_cloud.ObjectExistsRequest("annotationdocs\\one-page.docx", Common.myStorage)
            response = api.object_exists(request)
            
            print("Expected response type is ObjectExist: " + str(response))
        except groupdocs_annotation_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))