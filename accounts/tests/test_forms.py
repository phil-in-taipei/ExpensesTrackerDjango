from django.test import TestCase
from django.contrib.auth import get_user_model
from .. forms import RegisterForm, UserLoginForm


User = get_user_model()


class RegisterFormTests(TestCase):
    """Test the Login Form"""
    def test_valid_form(self):
        print("Test that the Register Form is Valid")
        data = {'username': 'TestUser2',
                'password1': 'testpassword',
                'password2': 'testpassword',
                }
        form = RegisterForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_username_exists(self):
        print("Test that the Register Form is Invalid -- username already exists")
        # the form is invalid because the user already exists
        user_obj = User.objects.create_user(
            username="TestUser1", password="testpassword")
        data = {'username': 'TestUser1',
                'password1': 'testpassword',
                'password2': 'testpassword',
                }
        form = RegisterForm(data=data)
        self.assertFalse(form.is_valid())

    def test_invalid_form_password_confirmation_fails(self):
        print("Test that the Register Form is Invalid -- password confirmation failure")
        # the form is invalid because the password is incorrect
        data = {'username': 'TestUser2',
                'password1': 'testpassword',
                'password2': 'incorrect_password',
                }
        form = RegisterForm(data=data)
        self.assertFalse(form.is_valid())


class UserLoginFormTests(TestCase):
    """Test the Login Form"""
    def test_valid_form(self):
        print("Test that the Login Form is Valid")
        user_obj = User.objects.create_user(
            username="TestUser1", password="testpassword")
        data = {'username': user_obj.username,
                'password': 'testpassword',
                }
        form = UserLoginForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_password_incorrect(self):
        print("Test that the Login Form is Invalid -- Incorrect Password")
        # the form is invalid because the password is incorrect
        user_obj = User.objects.create_user(
            username="TestUser1", password="testpassword")
        data = {'username': user_obj.username,
                'password': 'incorrect_password',
                }
        form = UserLoginForm(data=data)
        self.assertFalse(form.is_valid())

    def test_invalid_form_username_incorrect(self):
        print("Test that the Login Form is Invalid -- Incorrect Username")
        # the form is invalid because the username is incorrect
        user_obj = User.objects.create_user(
            username="TestUser1", password="testpassword")
        data = {'username': 'incorrect_username',
                'password': 'testpassword',
                }
        form = UserLoginForm(data=data)
        self.assertFalse(form.is_valid())
