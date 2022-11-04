from django.urls import path, include
from .views import base_views, editor_views, console_views


urlpatterns = [

    #base_views.py
    path("hello/", base_views.helloAPI),
    path("", base_views.get_lectures),
    path("<int:lecture_id>", base_views.get_assignments),
    path("<int:lecture_id>/assignment/<int:assignment_id>", base_views.get_problem),
    # path("<int:lecture_id>/assignment/<int:assignment_id>/problem/<int:problem_id>", base_views.show_problem),
    path("problem", base_views.info_problem),
    path('save/', editor_views.save_code),
    path('download/', editor_views.download_code),
    path('<str:user_id>/<int:problem_id>/', base_views.get_main_page),
    path('run/', console_views.run_code),
    path('grade/', console_views.grade_code),
]
