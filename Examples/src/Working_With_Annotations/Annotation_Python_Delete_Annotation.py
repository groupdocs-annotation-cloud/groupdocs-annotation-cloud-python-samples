# Import modules
import os

from groupdocs_annotation_cloud import *
import groupdocs_annotation_cloud

from Common_Utilities.Utils import Common_Utilities


class Annotation_Python_Delete_Annotation:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_AnnotateApi_Instance()
        
        try:           
            request = DeleteAnnotationsRequest("annotationdocs\\one-page.docx")
            api.delete_annotations(request)
            
            print("Expected response type is Void: Annotation deleted from document.")
        except ApiException as e:
            print("Exception when calling Annotation_Python_Delete_Annotation: {0}".format(e.message))