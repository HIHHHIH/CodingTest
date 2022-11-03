from django.urls import path, include
from .views import base_views
from .views import editor_view
urlpatterns = [

    #base_views.py
    path("hello/", base_views.helloAPI),
    path("", base_views.get_lectures),
    path("lecture/", base_views.get_assignments),
    path("assignment/", base_views.get_problem),
    path("problem/", base_views.info_problem),
    path('save/', editor_view.save_code),
    path('download/', editor_view.download_code)
]
