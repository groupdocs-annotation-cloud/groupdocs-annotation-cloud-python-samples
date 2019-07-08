# Import modules
import os

from groupdocs_annotation_cloud import *
import groupdocs_annotation_cloud

from Common_Utilities.Utils import Common_Utilities


class Annotation_Python_Get_PDF:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_AnnotateApi_Instance()
        
        try:           
            request = GetPdfRequest("annotationdocs\\one-page.docx")
            response = api.get_pdf(request)
            
            print("Expected response type is Stream: Document Length: " + str(os.path.getsize(response)))
        except ApiException as e:
            print("Exception when calling Annotation_Python_Get_PDF: {0}".format(e.message))