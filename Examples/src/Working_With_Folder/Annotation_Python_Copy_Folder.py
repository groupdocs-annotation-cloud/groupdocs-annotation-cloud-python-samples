# Import modules
import groupdocs_annotation_cloud

from Common_Utilities.Utils import Common_Utilities


class Annotation_Python_Copy_Folder:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_FolderApi_Instance()
        
        try:
            request = groupdocs_annotation_cloud.CopyFolderRequest("annotationdocs", "annotationdocs1", Common_Utilities.myStorage, Common_Utilities.myStorage)
            api.copy_folder(request)
            
            print("Expected response type is Void: 'annotationdocs' folder copied as 'annotationdocs1'.")
        except groupdocs_annotation_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))