from .views import TeacherViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', TeacherViewSet, basename='student')
urlpatterns = router.urls