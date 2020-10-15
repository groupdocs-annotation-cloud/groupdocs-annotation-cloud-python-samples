# Import modules
import groupdocs_annotation_cloud

from Common import Common

class StorageExist:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_annotation_cloud.StorageApi.from_config(Common.GetConfig())
        
        try:
            request = groupdocs_annotation_cloud.StorageExistsRequest(Common.myStorage)
            response = api.storage_exists(request)
            
            print("Expected response type is StorageExist: " + str(response))
        except groupdocs_annotation_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))