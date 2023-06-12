from django.contrib.auth import get_user_model
from django.test import TestCase

from income.models import IncomeSource

User = get_user_model()


class IncomeSourceModelTests(TestCase):
    """Test the Income Source Model"""

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            'testuser',
            'testpassword'
        )

        self.income_source = IncomeSource.objects.create(
            income_source_name='Test Income Source',
            user=self.user
        )

    def test_income_source_model_fields(self):
        """Test the Income Source fields"""
        print("Test the Income Source fields")
        self.assertEqual(self.income_source.user, self.user)
        self.assertEqual(self.income_source.income_source_name, 'Test Income Source')

    def test_income_source_model_str(self):
        """Test the Income Source string representation"""
        print("Test the Income Source representation")
        self.assertEqual(str(self.income_source), "{}: {}".format(
            self.income_source.user,
            self.income_source.income_source_name
        ).title())



