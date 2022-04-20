
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import UserViewSet

router = DefaultRouter()
router.register(r'', UserViewSet, basename='student')
#urlpatterns = router.urls

urlpatterns = [
  path('auth/', include('rest_auth.urls')),
]
urlpatterns += router.urls

'''
from .views import UserViewSet, ChangePasswordView
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'', UserViewSet, basename='student')
#urlpatterns = router.urls

urlpatterns = [
    path('changepassword/', ChangePasswordView.as_view(), name='changepassword'),
]

urlpatterns +=  router.urls
'''