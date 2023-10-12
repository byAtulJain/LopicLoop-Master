from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ResourceCard(models.Model):    
    language = models.CharField(max_length=30)
    headline = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=30)
    content = models.TextField()

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
