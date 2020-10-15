# Import modules
import groupdocs_annotation_cloud

from Common import Common

class CopyFile:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_annotation_cloud.FileApi.from_config(Common.GetConfig())
        
        try:
            request = groupdocs_annotation_cloud.CopyFileRequest("annotationdocs\\one-page.docx", "annotationdocs\\one-page-copied.docx", Common.myStorage, Common.myStorage)
            api.copy_file(request)
            
            print("Expected response type is Void: 'annotationdocs/one-page.docx' file copied as 'annotationdocs/one-page-copied.docx'.")
        except groupdocs_annotation_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))