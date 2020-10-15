# Import modules
from groupdocs_annotation_cloud import *
import groupdocs_annotation_cloud

from Common import Common

class AddAreaAnnotation:
    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_annotation_cloud.AnnotateApi.from_config(Common.GetConfig())
        
        try:        
            a1 = groupdocs_annotation_cloud.AnnotationInfo()
            a1.annotation_position = groupdocs_annotation_cloud.Point()
            a1.annotation_position.x = 1
            a1.annotation_position.y = 1
            a1.box = groupdocs_annotation_cloud.Rectangle()
            a1.box.x = 100
            a1.box.y = 100
            a1.box.width = 200
            a1.box.height = 100
            a1.page_number = 0
            a1.pen_color = 1201033
            a1.pen_style = "Solid"
            a1.pen_width = 1
            a1.opacity = 0.7
            a1.type = "Area"
            a1.text = "This is area annotation"
            a1.creator_name = "Anonym A."
    
            request = PostAnnotationsRequest("annotationdocs\\one-page.docx", [a1])
            api.post_annotations(request)
            
            print("AddAreaAnnotation: Area Annotation added.")
        except ApiException as e:
            print("Exception when calling AnnotateAPI: {0}".format(e.message))