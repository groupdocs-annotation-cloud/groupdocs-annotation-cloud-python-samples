# Import modules
import groupdocs_annotation_cloud

from Common_Utilities.Utils import Common_Utilities


class Annotation_Python_Get_Files_List:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_FolderApi_Instance()
        
        try:
            request = groupdocs_annotation_cloud.GetFilesListRequest("annotationdocs\\sample.docx", Common_Utilities.myStorage)
            response = api.get_files_list(request)
            
            print("Expected response type is FilesList: " + str(response))
        except groupdocs_annotation_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))