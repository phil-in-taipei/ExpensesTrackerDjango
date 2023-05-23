from django.test import TestCase
from django.contrib.auth import get_user_model

from .. models import UserProfile


class UserProfileModelTests(TestCase):
    """Test the Profile Model"""

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

    def test_profile_fields(self):
        """Test the profile fields"""
        print("Testing the profile fields")
        self.assertEqual(self.profile.email, 'tests@email.com')
        self.assertEqual(self.profile.surname, 'profile')
        self.assertEqual(self.profile.age, 50)
        self.assertEqual(self.profile.given_name, 'tests')

    def test_profile_model_str(self):
        """Test the profile string representation"""
        print("Testing the profile string representation")
        self.assertEqual(str(self.profile), self.profile.user.username)


