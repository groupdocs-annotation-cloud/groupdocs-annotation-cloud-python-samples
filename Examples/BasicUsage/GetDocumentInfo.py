# Import modules
from groupdocs_annotation_cloud import *
import groupdocs_annotation_cloud

from Common import Common

class GetDocumentInfo:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_annotation_cloud.InfoApi.from_config(Common.GetConfig())
        
        file_info = FileInfo()
        file_info.file_path = "annotationdocs\\one-page.docx"
        
        request = GetInfoRequest(file_info)
        response = api.get_info(request)
        
        print("Page count = " + str(len(response.pages)))