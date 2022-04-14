from django.urls import path
from . import views

urlpatterns = [
    path('', views.ClassroomViewSet.as_view({'get': 'list'}), name='Classroom'),
    path('add/', views.ClassroomViewSet.as_view({'post': 'create'}), name='NewClassroom'),
    path('<int:pk>/update/', views.ClassroomViewSet.as_view({'post': 'update'}), name='EditClassroom'),
    path('<int:pk>/delete/', views.ClassroomViewSet.as_view({'get': 'destroy'}), name='DeleteClassroom'),
    ]