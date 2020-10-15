# Import modules
from groupdocs_annotation_cloud import *
import groupdocs_annotation_cloud

from Common import Common

class GetAnnotations:
    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_annotation_cloud.AnnotateApi.from_config(Common.GetConfig())
        
        try:        
            request = GetImportRequest("annotationdocs\\one-page.docx")
            response = api.get_import(request)
            
            print("GetAnnotations: annotations count: " + str(len(response)))
        except ApiException as e:
            print("Exception when calling GetAnnotations: {0}".format(e.message))