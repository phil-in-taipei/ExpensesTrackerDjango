from django.test import TestCase
from django.contrib.auth import get_user_model

from income.forms import IncomeSourceForm
from income.models import IncomeSource

User = get_user_model()


class IncomeSourceFormTests(TestCase):
    """Test the Income Source Form"""

    def test_valid_form(self):
        print("Test that the Income Source Form is Valid")
        user = User.objects.create_user(
            username="TestUser1",
            password="testpassword"
        )

        data = {
            'income_source_name': "Test Income Source",
            'user': user
        }
        form = IncomeSourceForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        print("Test that the Income Source Form is Invalid")
        user = User.objects.create_user(
            username="TestUser1",
            password="testpassword"
        )
        data = {
            'incorrect_field': user
        }
        form = IncomeSourceForm(data=data)
        self.assertFalse(form.is_valid())
