from django.urls import reverse
from model_mommy import mommy
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from guardian.shortcuts import assign_perm


class UserTest(APITestCase):
    def setUp(self):
        self.user = mommy.make(get_user_model(), is_staff=True, post=User.PostType.ADMIN)
        self.client.force_login(self.user)

        self.teacher_group = mommy.make(Group, name=User.GroupType.TEACHER)
        self.data = {'username': '4450033841', 'password': '123', 'email': 'mohadese.zare69@gmail.com',
                     'first_name': 'Mohadese',
                     'last_name': 'Zare', 'nationalCode': 4450033841, 'school_name': 'Iran',
                     'post': User.PostType.TEACHER, 'groups': [self.teacher_group.id]}

    def test_user_access(self):
        self.user = mommy.make(get_user_model())
        self.client.force_login(self.user)
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertFalse(self.user.is_staff)

    def test_user_list(self):
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_teacher(self):
        response = self.client.post(reverse('user-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_user(self):
        # sample old data
        self.teacher = mommy.make(get_user_model(), post=User.PostType.TEACHER, groups=[self.teacher_group, ])
        # sample new data for update
        self.data = {'username': '4450033841', 'password': '123', 'email': 'mohadese.zare69@gmail.com',
                     'first_name': 'Mohadese',
                     'last_name': 'Zare', 'nationalCode': 4450033841, 'school_name': 'Iran',
                     'post': User.PostType.TEACHER, 'groups': [self.teacher_group.id]}
        response = self.client.put(reverse('user-detail', args=[self.teacher.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_user(self):
        # sample old data
        self.teacher = mommy.make(get_user_model(), post=User.PostType.TEACHER, groups=[self.teacher_group, ])

        response = self.client.delete(reverse('user-detail', args=[self.teacher.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
