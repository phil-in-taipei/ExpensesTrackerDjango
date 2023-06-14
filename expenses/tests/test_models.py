import datetime
from django.contrib.auth import get_user_model
from django.test import TestCase

from currencies.models import Currency
from expenses.models import Expense, SpendingRecord

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


class SpendingRecordTests(TestCase):
    """Test the Spending Record Model"""

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            'testuser',
            'testpassword'
        )

        self.currency = Currency.objects.create(
            currency_name="Test Currency",
            currency_code="TRY"
        )

        self.expense = Expense.objects.create(
            expense_name='Test Expense',
            user=self.user
        )

        self.spending_record = SpendingRecord.objects.create(
            amount=100.00,
            currency=self.currency,
            expense=self.expense
        )

        self.today = datetime.date.today()

    def test_spending_record_model_fields(self):
        """Test the Spending Record fields"""
        print("Test the Spending Record fields")
        self.assertEqual(self.spending_record.amount, 100)
        self.assertEqual(self.spending_record.currency, self.currency)
        self.assertEqual(self.spending_record.expense.expense_name, 'Test Expense')
        self.assertEqual(self.spending_record.expense.user, self.user)
        self.assertEqual(self.spending_record.date, self.today)

    def test_spending_record_model_str(self):
        """Test the Spending Record string representation"""
        print("Test the Spending Record string representation")
        self.assertEqual(str(self.spending_record), "{} | {} | Amount: {}".format(
            self.expense,
            self.spending_record.date,
            self.spending_record.amount,
        ).title())
