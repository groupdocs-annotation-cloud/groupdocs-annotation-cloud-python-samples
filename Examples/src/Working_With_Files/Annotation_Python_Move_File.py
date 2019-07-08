# Import modules
import groupdocs_annotation_cloud

from Common_Utilities.Utils import Common_Utilities


class Annotation_Python_Move_File:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_FileApi_Instance()
        
        try:
            request = groupdocs_annotation_cloud.MoveFileRequest("annotationdocs\\one-page.docx", "annotationdocs1\\one-page.docx", Common_Utilities.myStorage, Common_Utilities.myStorage)
            api.move_file(request)
            
            print("Expected response type is Void: 'annotationdocs/one-page.docx' file moved to 'annotationdocs1/one-page.docx'.")
        except groupdocs_annotation_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))