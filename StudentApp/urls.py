from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentViewSet.as_view({'get': 'list'}), name='Students'),
    path('add/', views.StudentViewSet.as_view({'post': 'create'}), name='NewStudents'),
    path('<int:pk>/update/', views.StudentViewSet.as_view({'post': 'update'}), name='EditStudents'),
    path('<int:pk>/delete/', views.StudentViewSet.as_view({'get': 'destroy'}), name='DeleteStudents'),
]