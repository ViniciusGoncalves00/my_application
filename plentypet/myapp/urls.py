from django.urls import path

from . import views

urlpatterns = [
    # path('courses/', views.course_list, name='course_list'),
    path("", views.home, name="home"),
    path("courses/<int:course_id>/", views.course_detail, name="course_detail"),
    # path('courses/<int:course_id>/lessons/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
]
