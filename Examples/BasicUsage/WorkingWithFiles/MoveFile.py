# Import modules
import groupdocs_annotation_cloud

from Common import Common

class MoveFile:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_annotation_cloud.FileApi.from_config(Common.GetConfig())
        
        try:
            request = groupdocs_annotation_cloud.MoveFileRequest("annotationdocs\\one-page.docx", "annotationdocs1\\one-page.docx", Common.myStorage, Common.myStorage)
            api.move_file(request)
            
            print("Expected response type is Void: 'annotationdocs/one-page.docx' file moved to 'annotationdocs1/one-page.docx'.")
        except groupdocs_annotation_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))