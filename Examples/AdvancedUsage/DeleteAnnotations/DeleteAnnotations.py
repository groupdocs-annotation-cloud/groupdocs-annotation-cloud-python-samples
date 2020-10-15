# Import modules
import os

from groupdocs_annotation_cloud import *
import groupdocs_annotation_cloud

from Common import Common

class DeleteAnnotations:
    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_annotation_cloud.AnnotateApi.from_config(Common.GetConfig())
        
        try:           
            request = DeleteAnnotationsRequest("annotationdocs\\one-page.docx")
            api.delete_annotations(request)
            
            print("DeleteAnnotations: Annotation deleted from document.")
        except ApiException as e:
            print("Exception when calling DeleteAnnotations: {0}".format(e.message))