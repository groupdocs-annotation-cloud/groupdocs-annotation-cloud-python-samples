# Import modules
from groupdocs_annotation_cloud import *
import groupdocs_annotation_cloud

from Common_Utilities.Utils import Common_Utilities


class Annotation_Python_DocumentInfo_File:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_InfoApi_Instance()
        
        try:            
            request = GetInfoRequest("annotationdocs\\one-page.docx", None)
            response = api.get_info(request)
            
            print("file_path: " + str(response))
        except ApiException as e:
            print("Exception when calling Annotation_Python_DocumentInfo_File: {0}".format(e.message))