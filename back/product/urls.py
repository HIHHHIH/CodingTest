from django.urls import path, include
from .views import base_views

urlpatterns = [

    #base_views.py
    path("hello/", base_views.helloAPI),
    path("random/<int:id>/", base_views.randomProblems),
    path("<int:id>/", base_views.specificProblems),
    path("student/<int:id>/", base_views.specificStudent),
    
]
