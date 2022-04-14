from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from .models import Course
from .serializers import CourseSerializer



@api_view(['GET'])
def ApiCourseview(request):
    api_urls = {
        'all_items': '/',
        'Search by Category': '/?category=category_name',
        'Search by Subcategory': '/?subcategory=category_name',
        'Add': '/add',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }

    return Response(api_urls)


@api_view(['POST'])
def add_Course(request):
    course = CourseSerializer(data=request.data)

    # validating for already existing data
    if Course.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if course.is_valid():
        course.save()
        return Response(course.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_Courses(request):
    # checking for the parameters from the URL
    if request.query_params:
        items = Course.objects.filter(**request.query_param.dict())
    else:
        items = Course.objects.all()

    # if there is something in items else raise error
    if items:
        data = CourseSerializer(items)
        return Response(data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_Course(request, pk):
    item = Course.objects.get(pk=pk)
    data = CourseSerializer(instance=item, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_Course(request, pk):
    item = Course.objects.get(pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
'''
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, permissions, views
from .models import Course
from .serializers import CourseSerializer

class CourseList(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class AddCourse(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

class UpdateCource(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

'''



