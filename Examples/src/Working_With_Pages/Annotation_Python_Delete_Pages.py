# Import modules
from groupdocs_annotation_cloud import *
import groupdocs_annotation_cloud

from Common_Utilities.Utils import Common_Utilities


class Annotation_Python_Delete_Pages:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_PreviewApi_Instance()
        
        try:            
            request = DeletePagesRequest("annotationdocs\\one-page.docx")
            api.delete_pages(request)
            
            print("Pages removed for file: 'annotationdocs\one-page.docx'")
        except ApiException as e:
            print("Exception when calling Annotation_Python_Delete_Pages: {0}".format(e.message))