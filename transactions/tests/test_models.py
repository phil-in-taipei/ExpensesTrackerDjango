import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase

from currencies.models import Currency
from financial_accounts.models import SavingsAccount, Bank
from income.models import IncomeSource
from transactions.models import Deposit, Withdrawal

User = get_user_model()
today = datetime.datetime.today()


class DepositModelTests(TestCase):
    """Test the Deposit Model"""

    def setUp(self):
        self.bank = Bank.objects.create(bank_name="Test Bank")
        self.currency = Currency.objects.create(
            currency_name="Test Currency",
            currency_code="TRY"
        )
        self.user = User.objects.create_user(
            'testuser',
            'testpassword'
        )
        self.income_source = IncomeSource.objects.create(
            income_source_name='Test Income Source',
            user=self.user
        )
        self.savings_account = SavingsAccount.objects.create(
            bank=self.bank,
            account_name="Test Savings Account",
            account_owner=self.user,
            currency=self.currency
        )
        self.deposit = Deposit.objects.create(
            amount=100.00,
            date=today,
            income_source=self.income_source,
            savings_account=self.savings_account
        )

    def test_deposit_model_fields(self):
        """Test the Deposit fields"""
        print("Test the Deposit fields")
        self.assertEqual(self.deposit.income_source, self.income_source)
        self.assertEqual(self.deposit.savings_account, self.savings_account)
        self.assertEqual(self.deposit.amount, 100.00)
        self.assertEqual(self.deposit.date, today)

    def test_deposit_model_str(self):
        """Test the Deposit string representation"""
        print("Test the Deposit representation")
        self.assertEqual(str(self.deposit), "{} | {} | Amount: {}".format(
            self.deposit.date,
            str(self.deposit.savings_account),
            self.deposit.amount,
        ).title())


class WithdrawalModelTests(TestCase):
    """Test the Withdrawal Model"""

    def setUp(self):
        self.bank = Bank.objects.create(bank_name="Test Bank")
        self.currency = Currency.objects.create(
            currency_name="Test Currency",
            currency_code="TRY"
        )
        self.user = User.objects.create_user(
            'testuser',
            'testpassword'
        )
        self.savings_account = SavingsAccount.objects.create(
            bank=self.bank,
            account_name="Test Savings Account",
            account_owner=self.user,
            currency=self.currency
        )
        self.withdrawal = Withdrawal.objects.create(
            amount=100.00,
            date=today,
            savings_account=self.savings_account
        )

    def test_withdrawal_model_fields(self):
        """Test the Withdrawal fields"""
        print("Test the Withdrawal fields")
        self.assertEqual(self.withdrawal.savings_account, self.savings_account)
        self.assertEqual(self.withdrawal.amount, 100.00)
        self.assertEqual(self.withdrawal.date, today)

    def test_withdrawal_model_str(self):
        """Test the Withdrawal string representation"""
        print("Test the Withdrawal representation")
        self.assertEqual(str(self.withdrawal), "{} | {} | Amount: {}".format(
            self.withdrawal.date,
            str(self.withdrawal.savings_account),
            self.withdrawal.amount,
        ).title())
