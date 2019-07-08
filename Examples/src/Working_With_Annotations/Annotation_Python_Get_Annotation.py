# Import modules
from groupdocs_annotation_cloud import *
import groupdocs_annotation_cloud

from Common_Utilities.Utils import Common_Utilities


class Annotation_Python_Get_Annotation:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_AnnotateApi_Instance()
        
        try:        
            request = GetImportRequest("annotationdocs\\one-page.docx")
            response = api.get_import(request)
            
            print("Expected response type is List<AnnotationInfo>: Count: " + str(len(response)))
        except ApiException as e:
            print("Exception when calling Annotation_Python_Get_Annotation: {0}".format(e.message))