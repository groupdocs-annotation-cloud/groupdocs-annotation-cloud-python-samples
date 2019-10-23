# Import modules
from groupdocs_annotation_cloud import *
import groupdocs_annotation_cloud

from Common_Utilities.Utils import Common_Utilities


class Annotation_Python_Add_TextUnderline_Annotation:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_AnnotateApi_Instance()
        
        try:        
            a1 = groupdocs_annotation_cloud.AnnotationInfo()
            a1.annotation_position = groupdocs_annotation_cloud.Point()
            a1.annotation_position.x = 852
            a1.annotation_position.y = 59.388262910798119
            a1.page_number = 2
            a1.font_color = 1201033
            a1.opacity = 0.7
            a1.type = "TextUnderline"
            a1.text = "This is text underline annotation"
            a1.creator_name = "Anonym A."
    
            request = PostAnnotationsRequest("annotationdocs\\ten-pages.docx", [a1])
            api.post_annotations(request)
            
            print("Expected response type is void: Text Underline Annotation added.")
        except ApiException as e:
            print("Exception when calling AnnotateAPI: {0}".format(e.message))