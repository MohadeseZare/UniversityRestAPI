from django.urls import path, include
from . import views
from rest_framework import routers

# define the router
#router = routers.DefaultRouter()

# define the router path and viewset to be used
#router.register(r'Courses', views.CourseViewSet)

urlpatterns = [
    path('', views.ApiCourseview, name='home'),
    path('add/', views.add_Course, name='add_Courses'),
    path('all/', views.view_Courses, name='view_Courses'),
    path('update/<int:pk>/', views.update_Course, name='update_Course'),
    path('Course/<int:pk>/delete/', views.delete_Course, name='delete_Course'),

]