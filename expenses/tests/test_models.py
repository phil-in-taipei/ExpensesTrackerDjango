from django.contrib.auth import get_user_model
from django.test import TestCase

from expenses.models import Expense

User = get_user_model()


class ExpenseModelTests(TestCase):
    """Test the Expense Model"""

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            'testuser',
            'testpassword'
        )

        self.expense = Expense.objects.create(
            expense_name='Test Expense',
            user=self.user
        )

    def test_expense_model_fields(self):
        """Test the Expense fields"""
        print("Test the Expense fields")
        self.assertEqual(self.expense.user, self.user)
        self.assertEqual(self.expense.expense_name, 'Test Expense')

    def test_expense_model_str(self):
        """Test the Expense string representation"""
        print("Test the Expense string representation")
        self.assertEqual(str(self.expense), "{}: {}".format(
            self.expense.user,
            self.expense.expense_name
        ).title())
