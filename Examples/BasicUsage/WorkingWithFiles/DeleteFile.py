# Import modules
import groupdocs_annotation_cloud

from Common import Common

class DeleteFile:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_annotation_cloud.FileApi.from_config(Common.GetConfig())
        
        try:
            request = groupdocs_annotation_cloud.DeleteFileRequest("annotationdocs1\\one-page.docx", Common.myStorage)
            api.delete_file(request)
            
            print("Expected response type is Void: 'annotationdocs1/one-page.docx' deleted.")
        except groupdocs_annotation_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))