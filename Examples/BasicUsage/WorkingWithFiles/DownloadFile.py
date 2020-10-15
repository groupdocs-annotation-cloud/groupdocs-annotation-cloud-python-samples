# Import modules
import groupdocs_annotation_cloud

from Common import Common

class DownloadFile:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_annotation_cloud.FileApi.from_config(Common.GetConfig())
        
        try:
            request = groupdocs_annotation_cloud.DownloadFileRequest("annotationdocs\\one-page.docx", Common.myStorage)
            response = api.download_file(request)
            
            print("Expected response type is Stream: " + str(len(response)))
        except groupdocs_annotation_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))