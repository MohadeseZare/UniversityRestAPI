from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Exercise
from ClassroomApp.models import Classroom
from django.contrib.auth import get_user_model
from model_mommy import mommy
from django.contrib.auth.models import Group
from UserApp.models import User
from faker import Faker

the_fake = Faker()

class ExerciseTests(APITestCase):

    def setUp(self):
        self.teacher_group = mommy.make(Group, name=User.Group_type.TEACHER)
        self.user = mommy.make(get_user_model(), semat=User.semat_type.TEACHER, groups=[self.teacher_group])
        self.client.force_login(self.user)

        self.classroom = mommy.make(Classroom, teacher=self.user)

        self.data = {'classroom': self.classroom.id, 'title': the_fake.text(), 'body': the_fake.text(),
                      'expiredate': the_fake.date_time()}




    def test_exercise_list(self):
        response = self.client.get(reverse('exercise-list'), )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_create_exercise(self):
        response = self.client.post(reverse('exercise-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_exercise(self):
        # Create new data for update
        self.exercise = mommy.make(Exercise, classroom=self.classroom)
        self.data = {'classroom': self.classroom.id, 'title': the_fake.text(), 'body': the_fake.text(),
                       'expiredate': the_fake.date_time()}
        response = self.client.put(reverse('exercise-detail', args=[self.exercise.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_exercise(self):
        self.news = mommy.make(Exercise, classroom=self.classroom)
        response = self.client.delete(reverse('exercise-detail', args=[self.news.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)