from django.test import TestCase
from django.contrib.auth import get_user_model

from .. models import UserProfile
from .. forms import UserProfileForm

User = get_user_model()


class UserProfileFormTests(TestCase):
    """Test the User Profile Form"""

    def test_valid_form(self):
        print("Test that the User Profile Form is Valid")
        user_obj = User.objects.create_user(
            username="TestUser1", password="testpassword")
        user_profile_obj = UserProfile.objects.create(
            user=user_obj,
            surname='McTest',
            given_name='Testy',
            email='test@gmx.com',
            age=40
        )
        data = {'surname': user_profile_obj.surname,
                'given_name': user_profile_obj.given_name,
                'email': user_profile_obj.email,
                'age': user_profile_obj.age,
                }
        form = UserProfileForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        print("Test that the User Profile Form is Invalid")
        # invalid because a string is passed in
        # for an integer value
        user_obj = User.objects.create_user(
            username="TestUser2", password="testpassword")
        user_profile_obj = UserProfile.objects.create(
            user=user_obj,
            surname='McTest',
            given_name='Testy',
            email='test@gmx.com',
            age=40
        )
        data = {'surname': user_profile_obj.surname,
                'given_name': user_profile_obj.given_name,
                'email': user_profile_obj.email,
                'age': 'forty',
                }
        form = UserProfileForm(data=data)
        self.assertFalse(form.is_valid())
