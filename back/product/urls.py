from django.urls import path, include
from .views import helloAPI, randomProblems

urlpatterns = [
    path("hello/", helloAPI),
    path("<int:id>/", randomProblems),
]
