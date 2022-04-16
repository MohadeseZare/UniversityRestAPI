from django.contrib import admin
from django.urls import path
from . import views
#from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', views.UserViewSet.as_view({'get': 'list'}), name='users'),
    #path('login/', LoginView.as_view(), name="login_url"),
    #path('logout/',LogoutView.as_view(next_page='dashboard'),name="logout"),
    path('add/', views.UserViewSet.as_view({'post': 'create'}), name='Newuser'),
    path('<int:pk>/update/', views.UserViewSet.as_view({'post': 'update'}), name='Edituser'),
    path('<int:pk>/delete/', views.UserViewSet.as_view({'get': 'destroy'}), name='Deleteuser'),
    ]