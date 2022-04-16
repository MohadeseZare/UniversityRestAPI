from django.urls import path
from .views import AnswerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', AnswerViewSet, basename='Answer')
urlpatterns = router.urls

'''
urlpatterns = [
    path('', views.AnswerViewSet.as_view({'get': 'list'}), name='Answers'),
    path('add/', views.AnswerViewSet.as_view({'post': 'create'}), name='NewAnswer'),
    path('<int:pk>/update/', views.AnswerViewSet.as_view({'post': 'update'}), name='EditAnswer'),
    path('<int:pk>/delete/', views.AnswerViewSet.as_view({'get': 'destroy'}), name='DeleteAnswer'),
    ]
    
'''