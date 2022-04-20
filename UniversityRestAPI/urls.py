"""UniversityRestAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('course/', include('CourseApp.urls')),
    path('exercise/', include('ExerciseApp.urls')),
    path('answer/',include('AnswerApp.urls')),
    #path('teacher/', include('TeacherApp.urls')),
   # path('student/', include('StudentApp.urls')),
    path('news/', include('NewsApp.urls')),
    path('classroom/', include('ClassroomApp.urls')),
    path('user/', include('UserApp.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)