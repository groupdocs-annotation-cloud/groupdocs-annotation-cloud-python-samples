# Import modules
import groupdocs_annotation_cloud

from Common import Common

class CopyFolder:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_annotation_cloud.FolderApi.from_config(Common.GetConfig())
        
        try:
            request = groupdocs_annotation_cloud.CopyFolderRequest("annotationdocs", "annotationdocs1", Common.myStorage, Common.myStorage)
            api.copy_folder(request)
            
            print("Expected response type is Void: 'annotationdocs' folder copied as 'annotationdocs1'.")
        except groupdocs_annotation_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))