# Import modules
from groupdocs_annotation_cloud import *
import groupdocs_annotation_cloud

from Common_Utilities.Utils import Common_Utilities


class Annotation_Python_Get_Pages:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_PreviewApi_Instance()
        
        try:            
            request = GetPagesRequest("annotationdocs\\one-page.docx", None, None, None, None, None, None, None)
            response = api.get_pages(request)
            
            print("Page Count: " + str(response.total_count))
        except ApiException as e:
            print("Exception when calling Annotation_Python_Get_Pages: {0}".format(e.message))