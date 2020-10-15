# Import modules
from groupdocs_annotation_cloud import *
import groupdocs_annotation_cloud

from Common import Common

class DeletePages:
    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_annotation_cloud.PreviewApi.from_config(Common.GetConfig())
        
        try:            
            request = DeletePagesRequest("annotationdocs\\one-page.docx")
            api.delete_pages(request)
            
            print("DeletePages: pages deleted")
        except ApiException as e:
            print("Exception when calling DeletePages: {0}".format(e.message))