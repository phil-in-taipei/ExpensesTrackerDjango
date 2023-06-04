from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .. models import UserProfile

User = get_user_model()


class UserProfileCreateViewPostTest(TestCase):
    """Test Create Profile Views"""
    def setUp(self):
        self.user = User.objects.create_user(
            'testuser',
            'testpassword'
        )
        self.client.force_login(self.user)

    def test_user_profile_create_post(self):
        print("Test User Profile Create View Form Post User Info")
        resp = self.client.post(reverse('user_profiles:profile_create'),
                                data={'given_name': 'tests', 'surname': 'profile',
                                      'age': 50, 'email': 'tests@email.com'},
                                content_type='application/x-www-form-urlencoded')

        self.assertEqual(resp.status_code, 302)
         #redirects to profile detail page after submitting form data
        self.assertEqual(resp.url, reverse('user_profiles:profile_detail'))


class UserProfileUpdateViewPostTest(TestCase):
    """Test Updating Profile View"""
    def setUp(self):
        self.user = User.objects.create_user(
            'testuser',
            'testpassword'
        )
        self.profile = UserProfile.objects.create(
            user=self.user,
            email='tests@email.com',
            given_name='tests',
            surname='profile',
            age=50
        )
        self.client.force_login(self.user)

    def test_user_profile_update_post(self):

        """Test User Profile Update View Form Post  User Info"""
        print("Test User Profile Update View Form Post User Info")
        resp = self.client.post(reverse('user_profiles:profile_update'),
                                data={'given_name': 'Testy', 'surname': 'McTEST',
                                      'age': 43, 'email': 'test111@gmx.com'},
                                content_type='application/x-www-form-urlencoded')

        self.assertEqual(resp.status_code, 302)
        # redirects to profile detail page after submitting form data
        self.assertEqual(resp.url, reverse('user_profiles:profile_detail'))
