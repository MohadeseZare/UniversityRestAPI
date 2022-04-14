from django.urls import path
from . import views

urlpatterns = [
    path('', views.ExerciseViewSet.as_view({'get': 'list'}), name='Exercises'),
    path('add/', views.ExerciseViewSet.as_view({'post': 'create'}), name='NewExercise'),
    path('<int:pk>/update/', views.ExerciseViewSet.as_view({'post': 'update'}), name='EditExercise'),
    path('<int:pk>/delete/', views.ExerciseViewSet.as_view({'get': 'destroy'}), name='DeleteExercise'),

]