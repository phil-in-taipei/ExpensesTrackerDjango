import datetime
from dateutil.relativedelta import relativedelta
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from currencies.models import Currency
from financial_accounts.models import SavingsAccount, Bank
from income.models import IncomeSource
from transactions.models import Deposit, Withdrawal
from utilities.date_utilities import get_name_of_current_month, get_list_of_months

today = datetime.date.today()
first_day_of_this_month = datetime.date(today.year, today.month, 1)
first_day_of_next_month = first_day_of_this_month + relativedelta(months=1)
last_day_of_this_month = first_day_of_next_month - relativedelta(days=1)
name_of_current_month = get_name_of_current_month()
User = get_user_model()


class TransactionsViewsTest(TestCase):
    """Test Transactions Views"""

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username="TestUser1",
            password="testpassword"
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
        self.test_deposit_1 = Deposit.objects.create(
            amount=100.00,
            date=first_day_of_this_month,
            income_source=self.income_source,
            savings_account=self.savings_account
        )
        self.test_deposit_2 = Deposit.objects.create(
            amount=200.00,
            date=last_day_of_this_month,
            income_source=self.income_source,
            savings_account=self.savings_account
        )
        self.test_withdrawal_1 = Withdrawal.objects.create(
            amount=100.00,
            date=first_day_of_this_month,
            savings_account=self.savings_account
        )
        self.test_withdrawal_2 = Withdrawal.objects.create(
            amount=200.00,
            date=last_day_of_this_month,
            savings_account=self.savings_account
        )

    def test_account_transactions_searched_month(self):
        """Test Transactions for a Specific Savings Account (current month) List View Display"""
        print("Test Transactions for a Specific Savings Account (current month) List View Display")
        url = reverse('transactions:account_transactions_searched_month',
                      kwargs={'month': today.month, 'year': today.year,
                              'savings_account_id': self.savings_account.pk})
        resp = self.client.get(url)
        #print(resp.content)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('Transactions', str(resp.content))
        self.assertIn('Deposit', str(resp.content))
        self.assertIn('Withdrawal', str(resp.content))
        self.assertIn('Source', str(resp.content))
        self.assertIn('Date', str(resp.content))
        self.assertIn('Account', str(resp.content))
        self.assertIn('Amount', str(resp.content))
        self.assertIn(name_of_current_month, str(resp.content))
        self.assertIn('100', str(resp.content))
        self.assertIn('200', str(resp.content))
        self.assertIn(str(today.year), str(resp.content))
        self.assertIn('Test Income Source', str(resp.content))
        #self.assertIn('Delete', str(resp.content))
        self.assertIn('Test Savings Account', str(resp.content))

    def test_make_deposit(self):
        """Test Make Deposit View Form Display"""
        print("Test Make Deposit View Form Display")
        url = reverse('transactions:make_deposit')
        resp = self.client.get(url)
        #print(resp.content)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('Make Deposit', str(resp.content))
        self.assertIn('Savings account', str(resp.content))
        self.assertIn('Income source', str(resp.content))
        self.assertIn('Date', str(resp.content))
        self.assertIn('Amount', str(resp.content))

    def test_make_withdrawal(self):
        """Test Make Withdrawal View Form Display"""
        print("Test Make Withdrawal View Form Display")
        url = reverse('transactions:make_withdrawal')
        resp = self.client.get(url)
        #print(resp.content)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('Make Withdrawal', str(resp.content))
        self.assertIn('Savings account', str(resp.content))
        self.assertIn('Date', str(resp.content))
        self.assertIn('Amount', str(resp.content))

    def test_search_account_transactions_by_month_and_year(self):
        """Test Search Savings Account Transactions By Month/Year View Form Display"""
        print("Test Search Savings Account Transactions By Month/Year View Form Display")
        url = reverse('transactions:search_account_transactions_by_month_and_year')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('Search Transactions', str(resp.content))
        self.assertIn('Test Savings Account', str(resp.content))
        month_list = get_list_of_months()
        for month in month_list:
            self.assertIn(month, str(resp.content))
        self.assertIn('2023', str(resp.content))
        self.assertIn('2024', str(resp.content))

    def test_search_user_deposits_by_month_and_year(self):
        """Test Search User Deposits By Month/Year View Form Display"""
        print("Test Search User Deposits By Month/Year View Form Display")
        url = reverse('transactions:search_user_deposits_by_month_and_year')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('Search Deposits', str(resp.content))
        month_list = get_list_of_months()
        for month in month_list:
            self.assertIn(month, str(resp.content))
        self.assertIn('2023', str(resp.content))
        self.assertIn('2024', str(resp.content))

    def test_search_user_withdrawals_by_month_and_year(self):
        """Test Search User Deposits By Month/Year View Form Display"""
        print("Test Search User Deposits By Month/Year View Form Display")
        url = reverse('transactions:search_user_withdrawals_by_month_and_year')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('Search Withdrawals', str(resp.content))
        month_list = get_list_of_months()
        for month in month_list:
            self.assertIn(month, str(resp.content))
        self.assertIn('2023', str(resp.content))
        self.assertIn('2024', str(resp.content))

    def test_user_deposits_current_month(self):
        """Test User's Deposits (current month) List View Display"""
        print("Test User's Deposits (current month) List View Display")
        url = reverse('transactions:user_deposits_current_month')
        resp = self.client.get(url)
        #print(resp.content)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('TestUser1\\\'s Deposits', str(resp.content))
        self.assertIn('Source', str(resp.content))
        self.assertIn('Date', str(resp.content))
        self.assertIn('Account', str(resp.content))
        self.assertIn('Amount', str(resp.content))
        self.assertIn(name_of_current_month, str(resp.content))
        self.assertIn('100', str(resp.content))
        self.assertIn('200', str(resp.content))
        self.assertIn(str(today.year), str(resp.content))
        self.assertIn('Test Income Source', str(resp.content))
        #self.assertIn('Delete', str(resp.content))
        self.assertIn('Test Savings Account', str(resp.content))

    def test_user_deposits_searched_month(self):
        """Test User Deposits for a Searched Month/Year List View Display"""
        print("Test User Deposits for a Searched Month/Year List View Display")
        url = reverse('transactions:user_deposits_searched_month',
                      kwargs={'month': today.month, 'year': today.year})
        resp = self.client.get(url)
        #print(resp.content)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('TestUser1\\\'s Deposits', str(resp.content))
        self.assertIn('Source', str(resp.content))
        self.assertIn('Date', str(resp.content))
        self.assertIn('Account', str(resp.content))
        self.assertIn('Amount', str(resp.content))
        self.assertIn(name_of_current_month, str(resp.content))
        self.assertIn('100', str(resp.content))
        self.assertIn('200', str(resp.content))
        self.assertIn(str(today.year), str(resp.content))
        self.assertIn('Test Income Source', str(resp.content))
        #self.assertIn('Delete', str(resp.content))
        self.assertIn('Test Savings Account', str(resp.content))

    def test_user_withdrawals_current_month(self):
        """Test User's Withdrawals (current month) List View Display"""
        print("Test User's Withdrawals (current month) List View Display")
        url = reverse('transactions:user_withdrawals_current_month')
        resp = self.client.get(url)
        #print(resp.content)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('TestUser1\\\'s Withdrawals', str(resp.content))
        self.assertIn('Date', str(resp.content))
        self.assertIn('Account', str(resp.content))
        self.assertIn('Amount', str(resp.content))
        self.assertIn(name_of_current_month, str(resp.content))
        self.assertIn('100', str(resp.content))
        self.assertIn('200', str(resp.content))
        self.assertIn(str(today.year), str(resp.content))
        #self.assertIn('Delete', str(resp.content))
        self.assertIn('Test Savings Account', str(resp.content))

    def test_user_withdrawals_searched_month(self):
        """Test User's Withdrawals for a Searched Month/Year List View Display"""
        print("Test User's Withdrawals for a Searched Month/Year List View Display")
        url = reverse('transactions:user_withdrawals_searched_month',
                      kwargs={'month': today.month, 'year': today.year})
        resp = self.client.get(url)
        #print(resp.content)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('TestUser1\\\'s Withdrawals', str(resp.content))
        self.assertIn('Date', str(resp.content))
        self.assertIn('Account', str(resp.content))
        self.assertIn('Amount', str(resp.content))
        self.assertIn(name_of_current_month, str(resp.content))
        self.assertIn('100', str(resp.content))
        self.assertIn('200', str(resp.content))
        self.assertIn(str(today.year), str(resp.content))
        #self.assertIn('Delete', str(resp.content))
        self.assertIn('Test Savings Account', str(resp.content))