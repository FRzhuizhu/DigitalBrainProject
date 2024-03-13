from django.db import models


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=8)
    email = models.EmailField()
    document = models.FileField(upload_to='uploads/')
