from .views import ExerciseViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ExerciseViewSet, basename='Exercise')
urlpatterns = router.urls