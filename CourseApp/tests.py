from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Course
from .serializers import CourseSerializer
from model_mommy import mommy
from django.contrib.auth import get_user_model

class CourseTests(APITestCase):

    def setUp(self):
        self.user = mommy.make(get_user_model(), is_staff=True)
        self.client.force_login(self.user)
        self.data = {'Title': 'Math'}

    def test_can_read_course_list(self):
        response = self.client.get(reverse('course-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_course(self):
        response = self.client.post(reverse('course-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.get().Title, 'Math')

    def test_update_course(self):
        old_course = Course.objects.create(Title='English')
        response = self.client.put(reverse('course-detail', args=[old_course.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Course.objects.get(id=old_course.id).Title, 'Math')

    def test_delete_course(self):
        old_course = Course.objects.create(Title='English')
        response = self.client.delete(reverse('course-detail', args=[old_course.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)




