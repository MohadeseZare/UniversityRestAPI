from django.urls import reverse
from model_mommy import mommy
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model


class UserTest(APITestCase):
    def setUp(self):
        super().setUpClass()
        self.user = mommy.make(get_user_model(), is_staff=True, post=User.PostType.ADMIN)
        self.client.force_login(self.user)

        self.teacher_group = mommy.make(Group, name=User.GroupType.TEACHER)
        self.data = {'username': '4450033841', 'password': '123', 'email': 'mohadese.zare69@gmail.com',
                     'first_name': 'Mohadese',
                     'last_name': 'Zare', 'nationalCode': 4450033841, 'school_name': 'Iran',
                     'post': User.PostType.TEACHER, 'groups': [self.teacher_group.id]}

    def test_login_superuser(self):
        user = User.objects.create_user('username', '123', is_staff=True)
        self.client.force_authenticate(user)
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_not_superuser(self):
        user = User.objects.create_user('username', '123')
        self.client.force_authenticate(user)
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_list(self):
        mommy.make(get_user_model(), post=User.PostType.TEACHER, groups=[self.teacher_group, ])
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        json = response.json()
        self.assertEqual(len(json), 3)

    def test_if_data_is_correct_then_signup(self):
        response = self.client.post(reverse('user-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = User.objects.last()
        self.assertEqual(user.username, '4450033841')
        self.assertEquals(user.check_password("123"), True)
        self.assertEqual(User.objects.count(), 3)

    def test_if_username_already_exists_dont_signup(self):
        # Prepare data with already saved user
        signup_dict = {
            'username': self.user.username,
            'password1': 'test_Pass',
            'password2': 'test_Pass',
        }
        # Make request
        response = self.client.post(reverse('user-list'), signup_dict)
        # Check status response
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            str(response.data['username'][0]),
            'A user with that username already exists.',
        )
        # Check database
        # Check that there is only one user with the saved username
        username_query = User.objects.filter(username=self.user.username)
        self.assertEqual(username_query.count(), 1)

    def test_update_user(self):
        # sample old data
        teacher = mommy.make(get_user_model(), post=User.PostType.TEACHER, groups=[self.teacher_group, ])
        # sample new data for update
        data = {'username': '4450033841', 'password': '123', 'email': 'mohadese.zare69@gmail.com',
                'first_name': 'Mohadese',
                'last_name': 'Zare', 'nationalCode': 4450033841, 'school_name': 'Iran',
                'post': User.PostType.TEACHER, 'groups': [self.teacher_group.id]}
        response = self.client.put(reverse('user-detail', args=[teacher.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user = User.objects.get(id=teacher.id)
        self.assertEqual(user.username, '4450033841')
        self.assertEquals(user.check_password("123"), True)

    def test_delete_user(self):
        # sample old data
        teacher = mommy.make(get_user_model(), post=User.PostType.TEACHER, groups=[self.teacher_group, ])

        response = self.client.delete(reverse('user-detail', args=[teacher.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # checked not exists
        user = User.objects.filter(id=teacher.id)
        self.assertEqual(user.count(), 0)
