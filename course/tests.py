from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Course
from model_mommy import mommy
from django.contrib.auth import get_user_model
from faker import Faker

the_fake = Faker()


class CourseTest(APITestCase):

    def setUp(self):
        self.user = mommy.make(get_user_model(), is_staff=True)
        self.client.force_login(self.user)
        self.data = {'title': 'test'}

    def test_user_access(self):
        user = mommy.make(get_user_model())
        self.client.force_login(user)
        response = self.client.get(reverse('course-list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertFalse(user.is_staff)

    def test_course_list(self):
        Course.objects.create(title=the_fake.text())
        response = self.client.get(reverse('course-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        json = response.json()
        self.assertEqual(len(json), 1)

    def test_create_course(self):
        response = self.client.post(reverse('course-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.count(), 1)
        course = Course.objects.get()
        self.assertEqual(course.title, 'test')

    def test_create_course_title_null(self):
        data = {'title': ''}
        response = self.client.post(reverse('course-list'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_course_title_unique(self):
        Course.objects.create(title='Math')
        data = {'title': 'Math'}
        response = self.client.post(reverse('course-list'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_course(self):
        fake_title = the_fake.text()
        old_course = Course.objects.create(title=fake_title)
        response = self.client.put(reverse('course-detail', args=[old_course.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(old_course.title, fake_title)

    def test_delete_course(self):
        old_course = Course.objects.create(title=the_fake.text())
        response = self.client.delete(reverse('course-detail', args=[old_course.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
