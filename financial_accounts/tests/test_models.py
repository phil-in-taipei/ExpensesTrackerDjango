from django.contrib.auth import get_user_model
from django.test import TestCase

from currencies.models import Currency
from .. models import Bank, SavingsAccount


class BankModelTests(TestCase):
    """Test the Bank Model"""

    def setUp(self):
        self.bank = Bank.objects.create(bank_name="Test Bank")

    def test_bank_fields(self):
        """Test the bank fields"""
        print("Test the bank fields")
        self.assertEqual(self.bank.bank_name, 'Test Bank')

    def test_bank_model_str(self):
        """Test the bank string representation"""
        print("Test the bank string representation")
        self.assertEqual(str(self.bank), self.bank.bank_name)


class SavingsAccountModelTests(TestCase):
    """Test the Savings Account Model"""

    def setUp(self):
        self.bank = Bank.objects.create(bank_name="Test Bank")
        self.currency = Currency.objects.create(
            currency_name="Test Currency",
            currency_code="TRY"
        )
        self.user = get_user_model().objects.create_user(
            'testuser',
            'testpassword'
        )
        self.savings_account = SavingsAccount.objects.create(
            bank=self.bank,
            account_name="Test Savings Account",
            account_owner=self.user,
            currency=self.currency
        )

    def test_savings_account_fields(self):
        """Test the savings account fields"""
        print("Test the savings account fields")
        self.assertEqual(self.savings_account.bank, self.bank)
        self.assertEqual(self.savings_account.account_name, "Test Savings Account")
        self.assertEqual(self.savings_account.account_owner, self.user)
        self.assertEqual(self.savings_account.account_balance, 0.00)
        self.assertEqual(self.savings_account.currency, self.currency)

    def test_savings_account_model_str(self):
        """Test the savings account string representation"""
        print("Test the savings account representation")
        self.assertEqual(str(self.savings_account), "{}: {} Account ({})".format(
            self.user,
            self.bank,
            self.savings_account.account_name
        ))
