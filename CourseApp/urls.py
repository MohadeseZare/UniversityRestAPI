from django.urls import path
from . import views

urlpatterns = [
    path('', views.CourseViewSet.as_view({'get': 'list'}), name='Courses'),
    path('add/', views.CourseViewSet.as_view({'post': 'create'}), name='NewCourses'),
    path('<int:pk>/update/', views.CourseViewSet.as_view({'post': 'update'}), name='EditCource'),
    path('<int:pk>/delete/', views.CourseViewSet.as_view({'get': 'destroy'}), name='DeleteCourse'),

]