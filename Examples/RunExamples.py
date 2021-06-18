# Import modules
import os
import groupdocs_annotation_cloud
from Common import Common

# Get your ClientId and ClientSecret at https://dashboard.groupdocs.cloud (free registration is required).
Common.client_id = "XXXXXXXXXXXXXXXX"
Common.client_secret = "XXXXXXXXXXXXXXXX"

Common.myStorage = "First Storage"

# Uploading sample test files from local disk to cloud storage
Common.UploadSampleFiles()

# BasicUsage examples

from BasicUsage.GetSupportedFormats import GetSupportedFormats
GetSupportedFormats.Run()

from BasicUsage.GetDocumentInfo import GetDocumentInfo
GetDocumentInfo.Run()

# AdvancedUsage examples

from AdvancedUsage.AddAnnotations.AddAreaAnnotation import AddAreaAnnotation
AddAreaAnnotation.Run()

from AdvancedUsage.AddAnnotations.AddArrowAnnotation import AddArrowAnnotation
AddArrowAnnotation.Run()
from AdvancedUsage.AddAnnotations.AddMultipleAnnotations import AddMultipleAnnotations
AddMultipleAnnotations.Run()
from AdvancedUsage.AddAnnotations.AddPointAnnotation import AddPointAnnotation
AddPointAnnotation.Run()
from AdvancedUsage.AddAnnotations.AddPolylineAnnotation import AddPolylineAnnotation
AddPolylineAnnotation.Run()
from AdvancedUsage.AddAnnotations.AddTextFieldAnnotation import AddTextFieldAnnotation
AddTextFieldAnnotation.Run()
from AdvancedUsage.AddAnnotations.AddTextRedactionAnnotation import AddTextRedactionAnnotation
AddTextRedactionAnnotation.Run()
from AdvancedUsage.AddAnnotations.AddTextReplacementAnnotation import AddTextReplacementAnnotation
AddTextReplacementAnnotation.Run()
from AdvancedUsage.AddAnnotations.AddTextStrikeoutAnnotation import AddTextStrikeoutAnnotation
AddTextStrikeoutAnnotation.Run()
from AdvancedUsage.AddAnnotations.AddTextUnderlineAnnotation import AddTextUnderlineAnnotation
AddTextUnderlineAnnotation.Run()
from AdvancedUsage.AddAnnotations.AddWatermarkAnnotation import AddWatermarkAnnotation
AddWatermarkAnnotation.Run()

from AdvancedUsage.ExtractAnnotations.ExtractAnnotations import ExtractAnnotations
ExtractAnnotations.Run()
from AdvancedUsage.AddAnnotationDirect.AddAnnotationDirect import AddAnnotationDirect
AddAnnotationDirect.Run()
from AdvancedUsage.RemoveAnnotations.RemoveAnnotations import RemoveAnnotations
RemoveAnnotations.Run()

from AdvancedUsage.DocumentPreview.GetPages import GetPages
GetPages.Run()
from AdvancedUsage.DocumentPreview.DeletePages import DeletePages
DeletePages.Run()
