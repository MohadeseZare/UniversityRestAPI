from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import News
from ClassroomApp.models import Classroom
from django.contrib.auth import get_user_model
from .serializers import NewsSerializer
from model_mommy import mommy
from django.contrib.auth.models import Group
from guardian.shortcuts import assign_perm

class NewsTests(APITestCase):

    def setUp(self):

        self.teacher_group = mommy.make(Group, name="teachergroup")
        self.user = mommy.make(get_user_model(), groups=[self.teacher_group])
        self.client.force_login(self.user)

        self.classroom = mommy.make(Classroom)
        self.news = mommy.make(News, Classroom=self.classroom)
        self.data = NewsSerializer(self.news).data


    def test_news_list(self):
        response = self.client.get(reverse('news-list'), )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_create_news(self):
        response = self.client.post(reverse('news-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_news(self):
        # Create new data for update
        self.classroom = mommy.make(Classroom)
        new_news = mommy.make(News, Classroom=self.classroom)
        # Convert to json
        self.data = NewsSerializer(new_news).data
        response = self.client.put(reverse('news-detail', args=[self.news.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_classroom(self):

        response = self.client.delete(reverse('news-detail', args=[self.news.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)