from django.urls import path
from .views import AnswerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', AnswerViewSet, basename='answer')
urlpatterns = router.urls
