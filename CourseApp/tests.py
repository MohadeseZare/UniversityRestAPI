from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Course
from model_mommy import mommy
from django.contrib.auth import get_user_model
from faker import Faker

the_fake = Faker()

class CourseTests(APITestCase):

    def setUp(self):
        self.user = mommy.make(get_user_model(), is_staff=True)
        self.client.force_login(self.user)
        self.data = {'Title': the_fake.text()}

    def test_permisstions(self):
        self.user = mommy.make(get_user_model())
        self.client.force_login(self.user)
        response = self.client.get(reverse('course-list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_can_read_course_list(self):
        response = self.client.get(reverse('course-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_course(self):
        response = self.client.post(reverse('course-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_course_title_null(self):
        self.data = {'Title': ''}
        response = self.client.post(reverse('course-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_course_title_unique(self):
        old_course = Course.objects.create(Title='Math')
        self.data = {'Title': 'Math'}
        response = self.client.post(reverse('course-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_course(self):
        old_course = Course.objects.create(Title=the_fake.text())
        response = self.client.put(reverse('course-detail', args=[old_course.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_course(self):
        old_course = Course.objects.create(Title=the_fake.text())
        response = self.client.delete(reverse('course-detail', args=[old_course.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)




