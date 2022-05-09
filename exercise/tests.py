from django.urls import reverse
from rest_framework import status, permissions
from rest_framework.test import APITestCase
from .models import Exercise
from classroom.models import Classroom
from django.contrib.auth import get_user_model
from model_mommy import mommy
from django.contrib.auth.models import Group
from user.models import User
from faker import Faker


class ExerciseTest(APITestCase):

    def setUp(self):
        self.the_fake = Faker()
        self.student_group = mommy.make(Group, name=User.GroupType.STUDENT)
        self.teacher_group = mommy.make(Group, name=User.GroupType.TEACHER)
        self.user = mommy.make(get_user_model(), post=User.PostType.TEACHER, groups=[self.teacher_group])
        self.client.force_login(self.user)

        self.classroom = mommy.make(Classroom, teacher=self.user)

        self.data = {'classroom': self.classroom.id, 'title': self.the_fake.text(), 'body': self.the_fake.text(),
                     'expire_date': self.the_fake.date_time()}

    def test_user_access(self):
        user = mommy.make(get_user_model(), post=User.PostType.STUDENT, groups=[self.student_group])
        self.client.force_login(user)
        response = self.client.post(reverse('exercise-list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertNotIn(self.teacher_group, user.groups.all())

    def test_user_access_safe_methods(self):
        user = mommy.make(get_user_model(), post=User.PostType.STUDENT, groups=[self.student_group])
        self.client.force_login(user)
        response = self.client.get(reverse('exercise-list'), )
        request = response.wsgi_request
        self.assertIn(request.method, permissions.SAFE_METHODS)

    def test_exercise_list_get_queryset_superuser(self):
        mommy.make(Exercise, classroom=self.classroom)
        superuser = mommy.make(get_user_model(), is_staff=True)
        self.client.force_login(superuser)
        response = self.client.get(reverse('exercise-list'), )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        json = response.json()
        self.assertEqual(len(json), 1)

    def create_sample_exercise_for_teacher(self):
        teacher_user = mommy.make(get_user_model(), post=User.PostType.TEACHER, groups=[self.teacher_group])
        classroom = mommy.make(Classroom, students=[self.user], teacher=teacher_user)
        mommy.make(Exercise, classroom=classroom, expire_date='2022-05-22T12:18:00Z')
        self.client.force_login(teacher_user)

    def test_exercise_get_queryset_teacher(self):
        # teacher one
        self.create_sample_exercise_for_teacher()
        # teacher Two
        self.create_sample_exercise_for_teacher()

        response = self.client.get(reverse('exercise-list'), )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        json = response.json()
        self.assertEqual(len(json), 1)

    def create_sample_exercise_for_student(self):
        mommy.make(Exercise, classroom=self.classroom)
        student_user = mommy.make(get_user_model(), post=User.PostType.STUDENT, groups=[self.student_group])
        classroom = mommy.make(Classroom, students=[student_user])
        mommy.make(Exercise, classroom=classroom, expire_date='2022-05-22T12:18:00Z')
        self.client.force_login(student_user)

    def test_exercise_get_queryset_student(self):
        self.create_sample_exercise_for_student()
        response = self.client.get(reverse('exercise-list'), )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        json = response.json()
        self.assertEqual(len(json), 1)

    def test_exercise_list(self):
        mommy.make(Exercise, classroom=self.classroom)
        response = self.client.get(reverse('exercise-list'), )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        json = response.json()
        self.assertEqual(len(json), 1)

    def test_create_exercise(self):
        mommy.make(Exercise, classroom=self.classroom)
        response = self.client.post(reverse('exercise-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # checked in database with id
        exercise = Exercise.objects.last()
        self.assertEqual(exercise.classroom, self.classroom)

    def test_create_exercise_classroom_null(self):
        data = {'classroom': '', 'title': self.the_fake.text(), 'body': self.the_fake.text(),
                'expire_date': self.the_fake.date_time()}
        response = self.client.post(reverse('exercise-list'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(str(response.data['classroom'][0]), 'This field may not be null.')

    def test_create_exercise_title_null(self):
        data = {'classroom': self.classroom.id, 'title': '', 'body': self.the_fake.text(),
                'expire_date': self.the_fake.date_time()}
        response = self.client.post(reverse('exercise-list'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(str(response.data['title'][0]), 'This field may not be blank.')

    def test_create_exercise_body_null(self):
        data = {'classroom': self.classroom.id, 'title': self.the_fake.text(), 'body': '',
                'expire_date': self.the_fake.date_time()}
        response = self.client.post(reverse('exercise-list'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(str(response.data['body'][0]), 'This field may not be blank.')

    def test_create_exercise_expired_null(self):
        data = {'classroom': self.classroom.id, 'title': self.the_fake.text(), 'body': self.the_fake.text(),
                'expire_date': ''}
        response = self.client.post(reverse('exercise-list'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Datetime has wrong format.", str(response.data['expire_date'][0]))

    def test_update_exercise(self):
        # Create new data for update
        exercise = mommy.make(Exercise, classroom=self.classroom)
        fake_body = self.the_fake.text()
        data = {'classroom': self.classroom.id, 'title': self.the_fake.text(), 'body': fake_body,
                'expire_date': self.the_fake.date_time()}
        response = self.client.put(reverse('exercise-detail', args=[exercise.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # checked in database with id
        exercise = Exercise.objects.get(id=exercise.id)
        self.assertEqual(exercise.classroom, self.classroom)
        self.assertEqual(exercise.body, fake_body)

    def test_delete_exercise(self):
        exercise = mommy.make(Exercise, classroom=self.classroom)
        response = self.client.delete(reverse('exercise-detail', args=[exercise.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # checked not exists
        exercise = Exercise.objects.filter(id=exercise.id)
        self.assertEqual(exercise.count(), 0)
