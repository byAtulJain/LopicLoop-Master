from django.db import models
from django.contrib.auth.models import User
# User
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rank = models.IntegerField(default=0)
    points =  models.IntegerField(default=0)
    def __str__(self):
        return self.user.username

# Learning Resources
class Language(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Topic(models.Model):    
    language = models.ForeignKey(Language,on_delete=models.CASCADE)
    heading = models.CharField(max_length=40)
    subheading = models.CharField(max_length=40)
    difficulty = models.CharField(max_length=30)
    content = models.TextField()
    tags = models.TextField()
    def __str__(self):
        return self.heading +' '+ self.language.name


# Challenges
class Problem(models.Model):
    title = models.CharField(max_length=40)
    statement = models.TextField()
    difficulty = models.CharField(max_length=30)
    points = models.IntegerField(default=0)
    def __str__(self):
        return self.title


class TestCase(models.Model):
    input_data = models.TextField()
    expected_ouput = models.TextField()
    hidden = models.BooleanField(default=False)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name="testcases")
   