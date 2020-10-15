# Import modules
import groupdocs_annotation_cloud

from Common import Common

class DeleteFolder:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_annotation_cloud.FolderApi.from_config(Common.GetConfig())
        
        try:
            request = groupdocs_annotation_cloud.DeleteFolderRequest("annotationdocs\\annotationdocs1", Common.myStorage, True)
            api.delete_folder(request)
            
            print("Expected response type is Void: 'annotationdocs/annotationdocs1' folder deleted recursively.")
        except groupdocs_annotation_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))