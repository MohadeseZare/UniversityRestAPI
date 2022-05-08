from .views import ExerciseViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ExerciseViewSet, basename='exercise')
urlpatterns = router.urls
