from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Classroom
from courseapp.models import Course
from django.contrib.auth import get_user_model
from model_mommy import mommy
from userapp.models import User
from guardian.shortcuts import assign_perm



class ClassroomTests(APITestCase):

    def setUp(self):
        self.user = mommy.make(get_user_model(), is_staff=True, post=User.PostType.ADMIN)
        self.client.force_login(self.user)

        self.course = mommy.make(Course)
        self.teacher = mommy.make(get_user_model(), post=User.PostType.TEACHER)
        self.student = mommy.make(get_user_model(), post=User.PostType.STUDENT)
        self.data = {'teacher': self.teacher.id, 'students': [self.student.id], 'course': self.course.id}

    def test_permisstions(self):
        self.user = mommy.make(get_user_model())
        self.client.force_login(self.user)
        response = self.client.get(reverse('Classroom-list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_classroom_list(self):
        response = self.client.get(reverse('Classroom-list'), )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_create_classroom(self):
        response = self.client.post(reverse('Classroom-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_classroom_teacher_null(self):
        self.data = {'teacher': '', 'students': [self.student.id], 'course': self.course.id}
        response = self.client.post(reverse('Classroom-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_classroom_students_null(self):
        self.data = {'teacher': '', 'students': [], 'course': self.course.id}
        response = self.client.post(reverse('Classroom-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_classroom_course_null(self):
        self.data = {'teacher': '', 'students': [self.student.id], 'course': ''}
        response = self.client.post(reverse('Classroom-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_classroom(self):
        # sample old data
        self.classroom = mommy.make(Classroom, course=self.course, teacher=self.teacher, students=[self.student])
        # Create new data for update
        self.course = mommy.make(Course)
        self.data = {'teacher': self.teacher.id, 'students': [self.student.id], 'course': self.course.id}
        response = self.client.put(reverse('Classroom-detail', args=[self.classroom.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_classroom(self):
        # sample old data
        self.classroom = mommy.make(Classroom, course=self.course, teacher=self.teacher, students=[self.student, ])

        response = self.client.delete(reverse('Classroom-detail', args=[self.classroom.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


"""
from guardian.shortcuts import assign_perm

 assign_perm('view_classroom', self.user, self.classroom)
        assign_perm('change_classroom', self.user, self.classroom)
        assign_perm('delete_classroom', self.user, self.classroom)
        assign_perm('add_classroom', self.user, self.classroom)
        """
