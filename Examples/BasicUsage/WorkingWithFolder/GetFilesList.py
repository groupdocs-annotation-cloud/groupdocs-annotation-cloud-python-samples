# Import modules
import groupdocs_annotation_cloud

from Common import Common

class GetFilesList:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_annotation_cloud.FolderApi.from_config(Common.GetConfig())
        
        try:
            request = groupdocs_annotation_cloud.GetFilesListRequest("annotationdocs\\sample.docx", Common.myStorage)
            response = api.get_files_list(request)
            
            print("Expected response type is FilesList: " + str(response))
        except groupdocs_annotation_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))