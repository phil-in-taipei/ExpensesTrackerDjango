import datetime
from django.test import TestCase
from django.contrib.auth import get_user_model

from currencies.models import Currency
from expenses.forms import ExpenseForm, SpendingRecordForm
from expenses.models import Expense

User = get_user_model()


class ExpenseFormTests(TestCase):
    """Test the Expense Form"""

    def test_valid_form(self):
        print("Test that the Expense Form is Valid")
        user = User.objects.create_user(
            username="TestUser1",
            password="testpassword"
        )

        data = {
            'expense_name': "Test Expense",
            'user': user
        }

        form = ExpenseForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        print("Test that the Expense Form is Invalid")
        user = User.objects.create_user(
            username="TestUser1",
            password="testpassword"
        )
        data = {
            'incorrect_field': user,
        }
        form = ExpenseForm(data=data)
        self.assertFalse(form.is_valid())


class SpendingRecordFormTests(TestCase):
    """Test the Spending Record Form"""

    def test_valid_form(self):
        print("Test that the Spending Record Form is Valid")
        user = User.objects.create_user(
            username="TestUser1",
            password="testpassword"
        )

        expense = Expense.objects.create(
            expense_name="Test Expense",
            user=user
        )

        currency = Currency.objects.create(
            currency_name="Test Currency",
            currency_code="TRY"
        )

        today = datetime.date.today()

        data = {
            'expense': expense,
            'currency': currency,
            'amount': 100.00,
            'date': today,
        }
        form = SpendingRecordForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        print("Test that the Spending Record Form is invalid")
        user = User.objects.create_user(
            username="TestUser1",
            password="testpassword"
        )

        expense = Expense.objects.create(
            expense_name="Test Expense",
            user=user
        )

        currency = Currency.objects.create(
            currency_name="Test Currency",
            currency_code="TRY"
        )

        today = datetime.date.today()

        data = {
            'amount': expense,
            'currency': currency,
            'expense': 100.00,
            'date': today,
        }
        form = SpendingRecordForm(data=data)
        self.assertFalse(form.is_valid())
