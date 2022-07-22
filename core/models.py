from django.db import models

# Create your models here.

class MLModelData(models.Model):
    
    user = models.CharField(null=True,blank=True,max_length=255)
    file = models.FileField(null=True,upload_to='datasets/')
    
    def __str__(self):
        return self.user
    
