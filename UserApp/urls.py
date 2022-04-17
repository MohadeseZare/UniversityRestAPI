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