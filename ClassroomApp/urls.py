
from .views import ClassroomViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ClassroomViewSet, basename='Classroom')
urlpatterns = router.urls
