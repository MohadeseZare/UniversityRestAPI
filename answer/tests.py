from django.urls import reverse
from rest_framework import status, permissions
from rest_framework.test import APITestCase
from exercise.models import Exercise
from .models import Answer
from classroom.models import Classroom
from django.contrib.auth import get_user_model
from model_mommy import mommy
from django.contrib.auth.models import Group
from user.models import User
from faker import Faker




class AnswerTest(APITestCase):

    def setUp(self):
        self.the_fake = Faker()
        self.teacher_group = mommy.make(Group, name=User.GroupType.TEACHER)
        self.student_group = mommy.make(Group, name=User.GroupType.STUDENT)
        self.user = mommy.make(get_user_model(), post=User.PostType.STUDENT, groups=[self.student_group])
        self.client.force_login(self.user)

        self.classroom = mommy.make(Classroom, students=[self.user])
        self.exercise = mommy.make(Exercise, classroom=self.classroom, expire_date='2022-05-22T12:18:00Z')
        self.data = {'exercise': self.exercise.id, 'body': self.the_fake.text()}

    def test_user_access(self):
        user = mommy.make(get_user_model(), post=User.PostType.TEACHER, groups=[self.teacher_group])
        self.client.force_login(user)
        response = self.client.post(reverse('answer-list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertNotIn(self.student_group, user.groups.all())

    def test_user_access_safe_methods(self):
        user = mommy.make(get_user_model(), post=User.PostType.TEACHER, groups=[self.teacher_group])
        self.client.force_login(user)
        response = self.client.get(reverse('answer-list'), )
        request = response.wsgi_request
        self.assertIn(request.method, permissions.SAFE_METHODS)

    def test_answer_list_get_queryset_superuser(self):
        Answer.objects.create(exercise=self.exercise, student=self.user, body=self.the_fake.text())
        superuser = mommy.make(get_user_model(), is_staff=True)
        self.client.force_login(superuser)
        response = self.client.get(reverse('answer-list'), )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        json = response.json()
        self.assertEqual(len(json), 1)

    def create_sample_answer_for_teacher(self):
        teacher_user = mommy.make(get_user_model(), post=User.PostType.TEACHER, groups=[self.teacher_group])
        classroom = mommy.make(Classroom, students=[self.user], teacher=teacher_user)
        exercise = mommy.make(Exercise, classroom=classroom, expire_date='2022-05-22T12:18:00Z')
        Answer.objects.create(exercise=exercise, student=self.user, body=self.the_fake.text())
        self.client.force_login(teacher_user)

    def test_answer_get_queryset_teacher(self):
        # teacher one
        self.create_sample_answer_for_teacher()
        # teacher Two
        self.create_sample_answer_for_teacher()

        response = self.client.get(reverse('answer-list'), )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        json = response.json()
        self.assertEqual(len(json), 1)

    def create_sample_answer_for_student(self):
        Answer.objects.create(exercise=self.exercise, student=self.user, body=self.the_fake.text())
        student_user = mommy.make(get_user_model(), post=User.PostType.STUDENT, groups=[self.student_group])
        classroom = mommy.make(Classroom, students=[student_user])
        exercise = mommy.make(Exercise, classroom=classroom, expire_date='2022-05-22T12:18:00Z')
        Answer.objects.create(exercise=exercise, student=student_user, body=self.the_fake.text())
        self.client.force_login(student_user)

    def test_answer_get_queryset_student(self):
        self.create_sample_answer_for_student()
        response = self.client.get(reverse('answer-list'), )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        json = response.json()
        self.assertEqual(len(json), 1)

    def test_create_answer(self):
        response = self.client.post(reverse('answer-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # checked new body with body
        answer = Answer.objects.last()
        self.assertEqual(answer.exercise, self.exercise)
        self.assertEqual(answer.student, self.user)

    def test_create_answer_exercise_null(self):
        data = {'exercise': '', 'body': self.the_fake.text()}
        response = self.client.post(reverse('answer-list'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(str(response.data['exercise'][0]), 'This field may not be null.')

    def test_create_answer_body_null(self):
        data = {'exercise': self.exercise.id, 'body': ''}
        response = self.client.post(reverse('answer-list'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(str(response.data['body'][0]), 'This field may not be blank.')

    def test_create_answer_exercise_timeout(self):
        exercise = mommy.make(Exercise, classroom=self.classroom, expire_date='2020-05-22T12:18:00Z')
        data = {'exercise': exercise.id, 'body': self.the_fake.text()}
        response = self.client.post(reverse('answer-list'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(str(response.data['non_field_errors'][0]), 'This exercise timeout.')

    def test_create_answer_more_than_one_answer(self):
        Answer.objects.create(exercise=self.exercise, student=self.user, body=self.the_fake.text())
        data = {'exercise': self.exercise.id, 'body': self.the_fake.text()}
        response = self.client.post(reverse('answer-list'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(str(response.data['non_field_errors'][0]), 'you cant add Two Answer for One exercise.')

    def test_update_answer(self):
        fake_body = self.the_fake.text()
        # Create new data for update
        answer = Answer.objects.create(exercise=self.exercise, student=self.user, body=self.the_fake.text())
        data = {'exercise': self.exercise.id, 'body': fake_body}
        response = self.client.put(reverse('answer-detail', args=[answer.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # checked new body with body
        answer = Answer.objects.get(id=answer.id)
        self.assertEqual(answer.body, fake_body)
        self.assertEqual(answer.exercise, self.exercise)
        self.assertEqual(answer.student, self.user)

    def test_delete_answer(self):
        answer = Answer.objects.create(exercise=self.exercise, student=self.user, body=self.the_fake.text())
        response = self.client.delete(reverse('answer-detail', args=[answer.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # checked not exists
        answer = Answer.objects.filter(id=answer.id)
        self.assertEqual(answer.count(), 0)
