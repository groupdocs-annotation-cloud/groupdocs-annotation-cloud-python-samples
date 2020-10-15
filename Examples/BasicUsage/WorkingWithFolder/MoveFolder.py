# Import modules
import groupdocs_annotation_cloud

from Common import Common

class MoveFolder:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_annotation_cloud.FolderApi.from_config(Common.GetConfig())
        
        try:
            request = groupdocs_annotation_cloud.MoveFolderRequest("annotationdocs1", "annotationdocs1\\annotationdocs", Common.myStorage, Common.myStorage)
            api.move_folder(request)
            
            print("Expected response type is Void: 'annotationdocs1' folder moved to 'annotationdocs/annotationdocs1'.")
        except groupdocs_annotation_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))