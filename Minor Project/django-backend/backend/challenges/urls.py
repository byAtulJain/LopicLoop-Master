from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("learningResources", views.learningResources, name="learningResources"),
    path("codeEditor", views.codeEditor, name="codeEditor"),
    path("challenges", views.challenges, name="challenges"),
    path("customRoom", views.customRoom, name="customRoom"),
    path("contact", views.contact, name="contact"),
    path("register", views.register, name="register"),
    path("logout",views.user_logout,name="user_logout")
]