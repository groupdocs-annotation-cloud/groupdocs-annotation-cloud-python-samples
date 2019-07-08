# Import modules
import groupdocs_annotation_cloud

from Common_Utilities.Utils import Common_Utilities


class Annotation_Python_Move_Folder:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_FolderApi_Instance()
        
        try:
            request = groupdocs_annotation_cloud.MoveFolderRequest("annotationdocs1", "annotationdocs1\\annotationdocs", Common_Utilities.myStorage, Common_Utilities.myStorage)
            api.move_folder(request)
            
            print("Expected response type is Void: 'annotationdocs1' folder moved to 'annotationdocs/annotationdocs1'.")
        except groupdocs_annotation_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))