from django.db import models
from .category import Category

class PhotoInfo(models.Model):
    tags = models.CharField(max_length=150, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.tags
