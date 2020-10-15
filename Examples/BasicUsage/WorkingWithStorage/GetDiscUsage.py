# Import modules
import groupdocs_annotation_cloud

from Common import Common

class GetDiscUsage:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_annotation_cloud.StorageApi.from_config(Common.GetConfig())
        
        try:
            request = groupdocs_annotation_cloud.GetDiscUsageRequest(Common.myStorage)
            response = api.get_disc_usage(request)
            
            print("Expected response type is DiscUsage: " + str(response))
        except groupdocs_annotation_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))