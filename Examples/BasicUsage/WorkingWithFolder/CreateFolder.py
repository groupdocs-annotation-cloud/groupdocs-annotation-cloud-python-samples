# Import modules
import groupdocs_annotation_cloud

from Common import Common

class CreateFolder:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_annotation_cloud.FolderApi.from_config(Common.GetConfig())
        
        try:
            request = groupdocs_annotation_cloud.CreateFolderRequest("Assembler", Common.myStorage)
            api.create_folder(request)
            
            print("Expected response type is Void: 'Assembler' folder created.")
        except groupdocs_annotation_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))