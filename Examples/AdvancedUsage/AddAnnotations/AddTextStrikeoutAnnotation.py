# Import modules
from groupdocs_annotation_cloud import *
import groupdocs_annotation_cloud

from Common import Common

class AddTextStrikeoutAnnotation:
    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_annotation_cloud.AnnotateApi.from_config(Common.GetConfig())
        
        try:        
            a1 = groupdocs_annotation_cloud.AnnotationInfo()
            p1 = groupdocs_annotation_cloud.Point()
            p1.x = 80
            p1.y = 730
            p2 = groupdocs_annotation_cloud.Point()
            p2.x = 240
            p2.y = 730
            p3 = groupdocs_annotation_cloud.Point()
            p3.x = 80
            p3.y = 650
            p4 = groupdocs_annotation_cloud.Point()
            p4.x = 240
            p4.y = 650
            a1.points = [p1, p2, p3, p4]
            a1.page_number = 0
            a1.font_color = 1201033
            a1.opacity = 0.7
            a1.type = "TextStrikeout"
            a1.text = "This is text strikeout annotation"
            a1.creator_name = "Anonym A."
    
            request = PostAnnotationsRequest("annotationdocs\\one-page.docx", [a1])
            api.post_annotations(request)
            
            print("AddTextStrikeoutAnnotation: Text Strikeout Annotation added.")
        except ApiException as e:
            print("Exception when calling AnnotateAPI: {0}".format(e.message))