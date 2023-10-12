from django.contrib import admin

# Register your models here.
from .models import ResourceCard, UserProfileInfo

admin.site.register(ResourceCard)   
admin.site.register(UserProfileInfo)