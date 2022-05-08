from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from exerciseapp.models import Exercise
from .models import Answer
from classroomapp.models import Classroom
from django.contrib.auth import get_user_model
from model_mommy import mommy
from django.contrib.auth.models import Group
from userapp.models import User
from faker import Faker

the_fake = Faker()


class AnswerTest(APITestCase):

    def setUp(self):
        self.student_group = mommy.make(Group, name=User.GroupType.STUDENT)
        self.user = mommy.make(get_user_model(), post=User.PostType.STUDENT, groups=[self.student_group])
        self.client.force_login(self.user)

        self.classroom = mommy.make(Classroom, students=[self.user])
        self.exercise = mommy.make(Exercise, classroom=self.classroom, expiredate='2022-05-22T12:18:00Z')
        self.data = {'exercise': self.exercise.id, 'body': the_fake.text()}

    def test_user_access(self):
        self.teacher_group = mommy.make(Group, name=User.GroupType.TEACHER)
        self.user = mommy.make(get_user_model(), post=User.PostType.TEACHER, groups=[self.teacher_group])
        self.client.force_login(self.user)
        response = self.client.post(reverse('answer-list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertNotIn(self.student_group, self.user.groups.all())

    def test_answer_list(self):
        response = self.client.get(reverse('answer-list'), )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_answer(self):
        response = self.client.post(reverse('answer-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_answer_exercise_null(self):
        self.data = {'exercise': '', 'body': the_fake.text()}
        response = self.client.post(reverse('answer-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_answer_body_null(self):
        self.data = {'exercise': self.exercise.id, 'body': ''}
        response = self.client.post(reverse('answer-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_answer_exercise_timeout(self):
        self.exercise = mommy.make(Exercise, classroom=self.classroom, expiredate='2020-05-22T12:18:00Z')
        self.data = {'exercise': self.exercise.id, 'body': the_fake.text()}
        response = self.client.post(reverse('answer-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_answer_More_than_One_Answer(self):
        self.answer = Answer.objects.create(exercise=self.exercise, student=self.user, body=the_fake.text())
        self.data = {'exercise': self.exercise.id, 'body': the_fake.text()}
        response = self.client.post(reverse('answer-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_answer(self):
        # Create new data for update
        self.answer = Answer.objects.create(exercise=self.exercise, student=self.user, body=the_fake.text())
        self.data = {'exercise': self.exercise.id, 'body': the_fake.text()}
        response = self.client.put(reverse('answer-detail', args=[self.answer.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_answer(self):
        self.answer = Answer.objects.create(exercise=self.exercise, student=self.user, body=the_fake.text())
        response = self.client.delete(reverse('answer-detail', args=[self.answer.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)