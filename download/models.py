from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Download(models.Model):
    def __str__(self):
        return self.title
        
    title = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    download_date = models.DateTimeField('Download date')