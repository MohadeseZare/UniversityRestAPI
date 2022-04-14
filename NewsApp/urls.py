from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsViewSet.as_view({'get': 'list'}), name='Newss'),
    path('add/', views.NewsViewSet.as_view({'post': 'create'}), name='NewNews'),
    path('<int:pk>/update/', views.NewsViewSet.as_view({'post': 'partial_update'}), name='EditNews'),
    path('<int:pk>/delete/', views.NewsViewSet.as_view({'get': 'destroy'}), name='DeleteNews'),
]