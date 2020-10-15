# Import modules
from groupdocs_annotation_cloud import *
import groupdocs_annotation_cloud

from Common import Common

class GetPages:
    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_annotation_cloud.PreviewApi.from_config(Common.GetConfig())
        
        try:            
            request = GetPagesRequest("annotationdocs\\one-page.docx", None, None, None, None, None, None, None)
            response = api.get_pages(request)
            
            print("GetPages: pages count = " + str(response.total_count))
        except ApiException as e:
            print("Exception when calling GetPages: {0}".format(e.message))