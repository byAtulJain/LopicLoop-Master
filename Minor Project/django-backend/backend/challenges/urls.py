from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    
    path("learningResources", views.learningResources, name="learningResources"),
    path("learningResources/<str:language>", views.languageTopics, name="languageTopics"),
    path("learningResources/<str:language>/<int:topicId>", views.topicContent, name="topicContent"),
    
    path("codeEditor", views.codeEditor, name="codeEditor"),

    path("challenges", views.challenges, name="challenges"),
    path("challenges/<str:difficulty>", views.allProblems, name="allProblems"),
    path("challenges/<str:difficulty>/<int:problemId>", views.problem, name="problem"),
    
    path("customRoom", views.customRoom, name="customRoom"),
    path("contact", views.contact, name="contact"),
    path("register", views.register, name="register"),
    path("logout",views.user_logout,name="user_logout"),
    
    #temporary for test case
    path('compile', views.compile_code, name='compile_code'),
]