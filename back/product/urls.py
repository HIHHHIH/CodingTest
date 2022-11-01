from django.urls import path, include
from .views import *

urlpatterns = [
    path("hello/", helloAPI),
    path("random/<int:id>/", randomProblems),
    path("<int:id>/", specificProblems),
    path("student/<int:id>/", specificStudent),
]
