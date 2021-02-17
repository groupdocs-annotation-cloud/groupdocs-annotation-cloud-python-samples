# Import modules
import os

from groupdocs_annotation_cloud import *
import groupdocs_annotation_cloud

from Common import Common

class RemoveAnnotations:
    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_annotation_cloud.AnnotateApi.from_config(Common.GetConfig())
        
        try:           
            file_info = FileInfo()
            file_info.file_path = "annotationdocs\\input.docx"
            options = RemoveOptions()
            options.file_info = file_info
            options.annotation_ids = [1, 2, 3]
            options.output_path = "Output\\output.docx"

            request = RemoveAnnotationsRequest(options)
            result = api.remove_annotations(request)

            print("RemoveAnnotations: Annotations removed: " + result['href'])
        except ApiException as e:
            print("Exception when calling RemoveAnnotations: {0}".format(e.message))