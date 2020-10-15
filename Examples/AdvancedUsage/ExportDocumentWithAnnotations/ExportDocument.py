# Import modules
import os

from groupdocs_annotation_cloud import *
import groupdocs_annotation_cloud

from Common import Common

class ExportDocument:
    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_annotation_cloud.AnnotateApi.from_config(Common.GetConfig())
        
        try:           
            request = GetExportRequest("annotationdocs\\one-page.docx", "Area,", None, None, None, None)
            response = api.get_export(request)
            
            print("ExportDocument: Document Length: " + str(os.path.getsize(response)))
        except ApiException as e:
            print("Exception when calling ExportDocument: {0}".format(e.message))