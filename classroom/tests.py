from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Classroom
from course.models import Course
from django.contrib.auth import get_user_model
from model_mommy import mommy
from user.models import User


class ClassroomTest(APITestCase):

    def setUp(self):
        self.user = mommy.make(get_user_model(), is_staff=True, post=User.PostType.ADMIN)
        self.client.force_login(self.user)

        self.course = mommy.make(Course)
        self.teacher = mommy.make(get_user_model(), post=User.PostType.TEACHER)
        self.student = mommy.make(get_user_model(), post=User.PostType.STUDENT)
        self.data = {'teacher': self.teacher.id, 'students': [self.student.id], 'course': self.course.id}

    def test_user_access(self):
        user = mommy.make(get_user_model())
        self.client.force_login(user)
        response = self.client.get(reverse('classroom-list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertFalse(user.is_staff)

    def test_classroom_list(self):
        response = self.client.get(reverse('classroom-list'), )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_classroom(self):
        response = self.client.post(reverse('classroom-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_classroom_teacher_null(self):
        data = {'teacher': '', 'students': [self.student.id], 'course': self.course.id}
        response = self.client.post(reverse('classroom-list'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_classroom_students_null(self):
        data = {'teacher': '', 'students': [], 'course': self.course.id}
        response = self.client.post(reverse('classroom-list'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_classroom_course_null(self):
        data = {'teacher': '', 'students': [self.student.id], 'course': ''}
        response = self.client.post(reverse('classroom-list'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_classroom(self):
        # sample old data
        classroom = mommy.make(Classroom, course=self.course, teacher=self.teacher, students=[self.student])
        # Create new data for update
        course = mommy.make(Course)
        data = {'teacher': self.teacher.id, 'students': [self.student.id], 'course': course.id}
        response = self.client.put(reverse('classroom-detail', args=[classroom.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_classroom(self):
        # sample old data
        classroom = mommy.make(Classroom, course=self.course, teacher=self.teacher, students=[self.student, ])
        response = self.client.delete(reverse('classroom-detail', args=[classroom.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
