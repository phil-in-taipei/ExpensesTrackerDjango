from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .. models import UserProfile


class UserProfileViewsTests(TestCase):
    """Test the Profile Views"""
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

        self.client.force_login(self.user)
        #self.client.force_login(self.user2)

    def test_user_profile_create(self):
        """Test User Profile Create View Form Display"""
        print("Test User Profile Create View Form Display")
        url = reverse('user_profiles:profile_create')
        resp = self.client.get(url)
        #print(resp.content)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('given_name', str(resp.content))
        self.assertIn('surname', str(resp.content))
        self.assertIn('age', str(resp.content))
        self.assertIn('email', str(resp.content))
        self.assertIn(self.user.username.title(), str(resp.content))

    def test_user_profile_detail(self):
        """Test User Profile Detail View"""
        print("Test User Profile Detail View")
        url = reverse('user_profiles:profile_detail')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('tests', str(resp.content))
        self.assertIn('profile', str(resp.content))
        self.assertIn(str(50), str(resp.content))
        self.assertIn('tests@email.com', str(resp.content))
        self.assertIn(self.user.username.title(), str(resp.content))

    def test_user_profile_update(self):
        """Test User Profile Update View Form Display With User Info"""
        print("Test User Profile Update View Form Display With User Info")
        url = reverse('user_profiles:profile_update')
        resp = self.client.get(url)
        # Form Fields
        self.assertEqual(resp.status_code, 200)
        self.assertIn('given_name', str(resp.content))
        self.assertIn('surname', str(resp.content))
        self.assertIn('age', str(resp.content))
        self.assertIn('email', str(resp.content))
        self.assertIn(self.user.username.title(), str(resp.content))

        # User Profile Info Pre-inserted into Form
        self.assertEqual(resp.status_code, 200)
        self.assertIn('tests', str(resp.content))
        self.assertIn('profile', str(resp.content))
        self.assertIn(str(50), str(resp.content))
        self.assertIn('tests@email.com', str(resp.content))
        self.assertIn(self.user.username.title(), str(resp.content))
