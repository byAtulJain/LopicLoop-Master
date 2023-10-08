from django.db import models

# Create your models here.
class ResourceCard(models.Model):
    language = models.CharField(max_length=30)
    headline = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=30)
    content = models.TextField()
