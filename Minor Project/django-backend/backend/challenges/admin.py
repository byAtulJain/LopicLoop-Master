from django.contrib import admin

# Register your models here.
from .models import UserProfileInfo, Language, Topic, Problem, TestCase

admin.site.register(UserProfileInfo)
admin.site.register(Language)
admin.site.register(Topic)
admin.site.register(Problem)
admin.site.register(TestCase)