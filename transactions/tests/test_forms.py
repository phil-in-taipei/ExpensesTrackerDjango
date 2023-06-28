import datetime

from django.test import TestCase
from django.contrib.auth import get_user_model

from currencies.models import Currency
from financial_accounts.models import Bank, SavingsAccount
from income.models import IncomeSource
from transactions.forms import DepositForm, WithdrawalForm

User = get_user_model()
today = datetime.date.today()


class DepositFormTests(TestCase):
    """Test the Deposit Form"""

    def test_valid_form(self):
        print("Test that the Deposit Form is Valid")
        bank = Bank.objects.create(bank_name="Test Bank")
        currency = Currency.objects.create(
            currency_name="Test Currency",
            currency_code="TRY"
        )
        user = User.objects.create_user(
            username="TestUser1",
            password="testpassword"
        )
        income_source = IncomeSource.objects.create(
            income_source_name='Test Income Source',
            user=user
        )
        savings_account = SavingsAccount.objects.create(
            bank=bank,
            account_name="Test Savings Account",
            account_owner=user,
            currency=currency
        )
        data = {
            'savings_account': savings_account,
            'income_source': income_source,
            'amount': 100.00,
            'date': today,
        }
        form = DepositForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        print("Test that the Deposit Form is invalid")
        bank = Bank.objects.create(bank_name="Test Bank")
        currency = Currency.objects.create(
            currency_name="Test Currency",
            currency_code="TRY"
        )
        user = User.objects.create_user(
            username="TestUser1",
            password="testpassword"
        )
        income_source = IncomeSource.objects.create(
            income_source_name='Test Income Source',
            user=user
        )
        savings_account = SavingsAccount.objects.create(
            bank=bank,
            account_name="Test Savings Account",
            account_owner=user,
            currency=currency
        )
        data = {
            'amount': savings_account,
            'income_source': income_source,
            'savings_account': 100.00,
            'date': today,
        }
        form = DepositForm(data=data)
        self.assertFalse(form.is_valid())


class WithdrawalFormTests(TestCase):
    """Test the Withdrawal Form"""

    def test_valid_form(self):
        print("Test that the Withdrawal Form is Valid")
        bank = Bank.objects.create(bank_name="Test Bank")
        currency = Currency.objects.create(
            currency_name="Test Currency",
            currency_code="TRY"
        )
        user = User.objects.create_user(
            username="TestUser1",
            password="testpassword"
        )
        savings_account = SavingsAccount.objects.create(
            bank=bank,
            account_name="Test Savings Account",
            account_owner=user,
            currency=currency
        )
        data = {
            'savings_account': savings_account,
            'date': today,
            'amount': 100.00
        }
        form = WithdrawalForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        print("Test that the Withdrawal Form is invalid")
        bank = Bank.objects.create(bank_name="Test Bank")
        currency = Currency.objects.create(
            currency_name="Test Currency",
            currency_code="TRY"
        )
        user = User.objects.create_user(
            username="TestUser1",
            password="testpassword"
        )
        savings_account = SavingsAccount.objects.create(
            bank=bank,
            account_name="Test Savings Account",
            account_owner=user,
            currency=currency
        )
        data = {
            'savings_account': savings_account,
            'date': today
        }
        form = WithdrawalForm(data=data)
        self.assertFalse(form.is_valid())
