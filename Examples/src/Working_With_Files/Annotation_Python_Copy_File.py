# Import modules
import groupdocs_annotation_cloud

from Common_Utilities.Utils import Common_Utilities


class Annotation_Python_Copy_File:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_FileApi_Instance()
        
        try:
            request = groupdocs_annotation_cloud.CopyFileRequest("annotationdocs\\one-page.docx", "annotationdocs\\one-page-copied.docx", Common_Utilities.myStorage, Common_Utilities.myStorage)
            api.copy_file(request)
            
            print("Expected response type is Void: 'annotationdocs/one-page.docx' file copied as 'annotationdocs/one-page-copied.docx'.")
        except groupdocs_annotation_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))