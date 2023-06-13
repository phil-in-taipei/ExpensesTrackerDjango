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
                                      'age': 50, 'email': 'tests@email.com'})
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.url, reverse('user_profiles:profile_detail'))
        created_profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(created_profile.given_name, 'tests')
        self.assertEqual(created_profile.surname, 'profile')
        self.assertEqual(created_profile.age, 50)
        self.assertEqual(created_profile.email, 'tests@email.com')


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

        """Test User Profile Update View Form Post User Info"""
        print("Test User Profile Update View Form Post User Info")
        resp = self.client.post(reverse('user_profiles:profile_update'),
                                data={'given_name': 'Testy', 'surname': 'McTEST',
                                      'age': 43, 'email': 'test111@gmx.com'})
        self.assertEqual(resp.status_code, 302)
        # redirects to profile detail page after submitting form data
        self.assertEqual(resp.url, reverse('user_profiles:profile_detail'))
        updated_profile = UserProfile.objects.get(id=self.profile.id)
        self.assertEqual(updated_profile.given_name, 'Testy')
        self.assertEqual(updated_profile.surname, 'McTEST')
        self.assertEqual(updated_profile.age, 43)
        self.assertEqual(updated_profile.email, 'test111@gmx.com')


