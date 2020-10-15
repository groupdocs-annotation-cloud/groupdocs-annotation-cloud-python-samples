# Import modules
import groupdocs_annotation_cloud

from Common import Common

class UploadFile:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_annotation_cloud.FileApi.from_config(Common.GetConfig())
        
        try:
            request = groupdocs_annotation_cloud.UploadFileRequest("annotationdocs\\one-page.docx", "D:\\ewspace\\GroupDocs.Annotation.Cloud.Python.Examples\\src\\Resources\\annotationdocs\\one-page.docx", Common.myStorage)
            response = api.upload_file(request)
            
            print("Expected response type is FilesUploadResult: " + str(response))
        except groupdocs_annotation_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))