from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from user_profiles.models import UserProfile


class AccountsViewsTests(TestCase):
    """Test the Accounts Views"""
    def setUp(self):
        self.user = get_user_model().objects.create_user(
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

    def test_login(self):
        """Test Login View Form Display"""
        print("Test Login View Form Display")
        url = reverse('accounts:login')
        resp = self.client.get(url)
        #print(resp.content)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('username', str(resp.content))
        self.assertIn('password', str(resp.content))

    def test_register(self):
        """Test Register View Form Display"""
        print("Test Register View Form Display")
        url = reverse('accounts:register')
        resp = self.client.get(url)
        print(resp.content)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('Username', str(resp.content))
        self.assertIn('Password', str(resp.content))
        self.assertIn('Password confirmation', str(resp.content))

