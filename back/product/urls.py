from django.urls import path, include
from .views import base_views, editor_views, console_views


urlpatterns = [

    #base_views.py
    path("hello/", base_views.helloAPI),
    path("", base_views.get_lectures),
    path("lecture/", base_views.get_assignments),
    path("assignment/", base_views.get_problem),
    # path("<int:lecture_id>/assignment/<int:assignment_id>/problem/<int:problem_id>", base_views.show_problem),
    path("problem/", base_views.info_problem),
    path("testcase/", base_views.run_specific_testcase),

    path('recent/<int:user_id>/', base_views.get_recent),

    path('save/', editor_views.save_code),

    path('<str:user_id>/<int:problem_id>/', base_views.get_main_page),

    path('run/', console_views.run_code),
    path('grade/', console_views.grade_code),
    path('submit/',console_views.submit_code),

    path('delete/', base_views.delete_session),
]
