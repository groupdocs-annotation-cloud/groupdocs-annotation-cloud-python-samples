# Import modules
from groupdocs_annotation_cloud import *
import groupdocs_annotation_cloud

from Common import Common

class AddMultipleAnnotations:
    
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
            a1.type = "Distance"
            a1.text = "This is distance annotation"
            a1.creator_name = "Anonym A."
    
            a2 = groupdocs_annotation_cloud.AnnotationInfo()
            a2.annotation_position = groupdocs_annotation_cloud.Point()
            a2.annotation_position.x = 1
            a2.annotation_position.y = 1
            a2.box = groupdocs_annotation_cloud.Rectangle()
            a2.box.x = 100
            a2.box.y = 100
            a2.box.width = 200
            a2.box.height = 100
            a2.page_number = 2
            a2.pen_color = 1201033
            a2.pen_style = "Solid"
            a2.pen_width = 1
            a2.opacity = 0.7
            a2.type = "Area"
            a2.text = "This is area annotation"
            a2.creator_name = "Anonym A."
    
            a3 = groupdocs_annotation_cloud.AnnotationInfo()
            a3.annotation_position = groupdocs_annotation_cloud.Point()
            a3.annotation_position.x = 1
            a3.annotation_position.y = 1
            a3.box = groupdocs_annotation_cloud.Rectangle()
            a3.box.x = 100
            a3.box.y = 100
            a3.box.width = 200
            a3.box.height = 100
            a3.page_number = 4
            a3.opacity = 0.7
            a3.type = "Point"
            a3.text = "This is point annotation"
            a3.creator_name = "Anonym A."
    
            a4 = groupdocs_annotation_cloud.AnnotationInfo()
            a4.annotation_position = groupdocs_annotation_cloud.Point()
            a4.annotation_position.x = 1
            a4.annotation_position.y = 1
            a4.box = groupdocs_annotation_cloud.Rectangle()
            a4.box.x = 100
            a4.box.y = 100
            a4.box.width = 200
            a4.box.height = 100
            a4.page_number = 5
            a4.pen_color = 1201033
            a4.pen_style = "Solid"
            a4.pen_width = 1
            a4.opacity = 0.7
            a4.type = "Arrow"
            a4.text = "This is arrow annotation"
            a4.creator_name = "Anonym A."
        
            file_info = FileInfo()
            file_info.file_path = "annotationdocs\\ten-pages.docx"
            options = AnnotateOptions()
            options.file_info = file_info
            options.annotations = [a1, a2, a3, a4]
            options.output_path = "Output\\output.docx"

            request = AnnotateRequest(options)
            result = api.annotate(request)         

            print("AddMultipleAnnotations: Multiple Annotations added: " + result['href'])
        except ApiException as e:
            print("Exception when calling AnnotateAPI: {0}".format(e.message))