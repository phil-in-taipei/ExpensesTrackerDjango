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

    def test_user_profile_detail_view(self):
        """Test User Profile Detail View"""
        print("Testing profile detail view")
        url = reverse('user_profiles:profile_detail')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.profile.given_name, str(resp.content))
        self.assertIn(self.profile.surname, str(resp.content))
        self.assertIn(str(self.profile.age), str(resp.content))
        self.assertIn(self.profile.email, str(resp.content))
