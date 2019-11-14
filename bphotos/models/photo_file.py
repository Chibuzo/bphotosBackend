from django.db import models
from .photo_info import PhotoInfo

class PhotoFile(models.Model):
    filename = models.CharField(max_length=100)
    photo_info_id = models.ForeignKey(PhotoInfo, on_delete=models.CASCADE)