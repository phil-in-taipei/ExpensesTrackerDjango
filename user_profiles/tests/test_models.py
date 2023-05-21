from django.test import TestCase
from django.contrib.auth import get_user_model

from .. models import UserProfile


def get_test_user(username):
    return get_user_model().objects.create_user(
        username=username,
        password='testpassword'
        )


class UserProfileModelTests(TestCase):
    """Test the Profile Model"""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'testuser',
            'testpassword'
        )

    def test_profile_fields(self):
        """Test the profile fields"""
        profile = UserProfile.objects.get(user=self.user)
        profile.email = 'tests@email.com'
        profile.surname = 'profile'
        profile.age = 50
        profile.given_name = 'tests'
        profile.save()
        modified_profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(modified_profile.email, 'tests@email.com')
        self.assertEqual(modified_profile.surname, 'profile')
        self.assertEqual(modified_profile.age, 50)
        self.assertEqual(modified_profile.given_name, 'tests')

    def test_profile_model_str(self):
        """Test the profile string representation"""
        profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(str(profile), profile.user.username)


