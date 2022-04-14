from django.urls import path
from . import views

urlpatterns = [
    path('', views.TeacherViewSet.as_view({'get': 'list'}), name='Teachers'),
    path('add/', views.TeacherViewSet.as_view({'post': 'create'}), name='NewTeacher'),
    path('<int:pk>/update/', views.TeacherViewSet.as_view({'post': 'update'}), name='EditTeacher'),
    path('<int:pk>/delete/', views.TeacherViewSet.as_view({'get': 'destroy'}), name='DeleteTeacher'),
]