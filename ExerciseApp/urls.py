from .views import ExerciseViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'', ExerciseViewSet, basename='exercise')
urlpatterns = router.urls

