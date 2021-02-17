# Import modules
from groupdocs_annotation_cloud import *
import groupdocs_annotation_cloud

from Common import Common

class ExtractAnnotations:
    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_annotation_cloud.AnnotateApi.from_config(Common.GetConfig())
        
        try:        
            file_info = FileInfo()
            file_info.file_path = "annotationdocs\\input.docx"

            request = ExtractRequest(file_info)
            result = api.extract(request)        
            
            print("ExtractAnnotations: annotations count: " + str(len(result)))
        except ApiException as e:
            print("Exception when calling ExtractAnnotations: {0}".format(e.message))