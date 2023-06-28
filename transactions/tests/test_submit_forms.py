from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from currencies.models import Currency
from financial_accounts.models import Bank, SavingsAccount
from income.models import IncomeSource

today = datetime.today()
User = get_user_model()


class MakeTransactionsViewsPostTest(TestCase):
    """Test Make Deposit and Withdrawal View Form Submission"""
    def setUp(self):
        self.user = User.objects.create_user(
            'testuser',
            'testpassword'
        )
        self.client.force_login(self.user)
        self.bank = Bank.objects.create(bank_name="Test Bank")
        self.currency = Currency.objects.create(
            currency_name="Test Currency",
            currency_code="TRY"
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

    def test_make_deposit_post(self):
        print("Test Make Deposit View Form Post")
        today_str = F"{today.year}-{today.month}-{today.day}"
        data = {
            'date': today_str,
            'income_source': str(self.income_source.pk),
            'savings_account': str(self.savings_account.pk),
            'amount': 100.00
        }
        resp = self.client.post(reverse('transactions:make_deposit'),
                                data=data)
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.url, reverse('transactions:user_deposits_current_month'))

    def test_make_withdrawal_post(self):
        print("Test Make Withdrawal View Form Post")
        today_str = F"{today.year}-{today.month}-{today.day}"
        data = {
            'date': today_str,
            'savings_account': str(self.savings_account.pk),
            'amount': 100.00
        }
        resp = self.client.post(reverse('transactions:make_withdrawal'),
                                data=data)
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.url, reverse('transactions:user_withdrawals_current_month'))

