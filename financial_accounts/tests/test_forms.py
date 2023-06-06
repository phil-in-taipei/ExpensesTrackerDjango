from django.test import TestCase
from django.contrib.auth import get_user_model

from currencies.models import Currency
from financial_accounts.forms import SavingsAccountCreateForm
from financial_accounts.models import Bank, SavingsAccount

User = get_user_model()


class SavingsAccountCreateFormTests(TestCase):
    """Test the Savings Account Form"""

    def test_valid_form(self):
        print("Test that the Savings Account Form is Valid")
        user = User.objects.create_user(
            username="TestUser1",
            password="testpassword"
        )
        bank = Bank.objects.create(bank_name="Test Bank")
        currency = Currency.objects.create(
            currency_name="Test Currency",
            currency_code="TRY"
        )
        savings_account = SavingsAccount.objects.create(
            bank=bank,
            account_name="Test Savings Account",
            account_owner=user,
            currency=currency
        )
        data = {'bank': bank,
                'account_name': savings_account.account_name,
                'currency': currency,
                }
        form = SavingsAccountCreateForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        print("Test that the Savings Account Form is Invalid")
        # invalid because a string is passed in
        # for a bank objects value
        user = User.objects.create_user(
            username="TestUser1",
            password="testpassword"
        )
        bank = Bank.objects.create(bank_name="Test Bank")
        currency = Currency.objects.create(
            currency_name="Test Currency",
            currency_code="TRY"
        )
        savings_account = SavingsAccount.objects.create(
            bank=bank,
            account_name="Test Savings Account",
            account_owner=user,
            currency=currency
        )
        data = {'bank': "Test Bank",
                'account_name': savings_account.account_name,
                'currency': currency,
                }
        form = SavingsAccountCreateForm(data=data)
        self.assertFalse(form.is_valid())
