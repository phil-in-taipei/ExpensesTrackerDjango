from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from currencies.models import Currency
from financial_accounts.models import Bank, SavingsAccount

User = get_user_model()


class FinancialAccountsViewsTest(TestCase):
    """Test Financial Accounts Views"""

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username="TestUser1",
            password="testpassword"
        )
        self.client.force_login(self.user)
        self.test_bank_1 = Bank.objects.create(bank_name="Test Bank 1")
        self.test_bank_2 = Bank.objects.create(bank_name="Test Bank 2")
        self.currency = Currency.objects.create(
            currency_name="Test Currency",
            currency_code="TRY"
        )
        self.test_savings_account_1 = SavingsAccount.objects.create(
            account_owner=self.user,
            bank=self.test_bank_1,
            currency=self.currency,
            account_name="Test Account 1"
        )

        self.test_savings_account_2 = SavingsAccount.objects.create(
            account_owner=self.user,
            bank=self.test_bank_2,
            currency=self.currency,
            account_name="Test Account 2"
        )

    def test_create_savings_account(self):
        """Test Create Savings Account View Form Display"""
        print("Test Create Savings Account View Form Display")
        url = reverse('financial_accounts:create_savings_account')
        resp = self.client.get(url)
        #print(resp.content)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('Create Savings Account', str(resp.content))
        self.assertIn('Bank', str(resp.content))
        self.assertIn('Account name', str(resp.content))
        self.assertIn('Currency', str(resp.content))

    def test_update_savings_account(self):
        """Test Update Savings Account View Form Display"""
        print("Test Update Savings Account View Form Display")
        url = reverse('financial_accounts:update_savings_account',
                      args=[self.test_savings_account_1.id])
        resp = self.client.get(url)
        #print(resp.content)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('Update ' + str(self.test_savings_account_1), str(resp.content))
        self.assertIn('Account name', str(resp.content))
        self.assertIn('Account balance', str(resp.content))

    def test_user_savings_accounts(self):
        """Test User's Savings Account View Display"""
        print("Test User's Savings Account View Display")
        url = reverse('financial_accounts:user_savings_accounts')
        resp = self.client.get(url)
        #print(resp.content)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('TestUser1\\\'s Accounts', str(resp.content))
        self.assertIn('Bank', str(resp.content))
        self.assertIn('Account Name', str(resp.content))
        self.assertIn('Currency', str(resp.content))
        self.assertIn('Balance', str(resp.content))
        self.assertIn('Edit', str(resp.content))

        self.assertIn('Test Bank 1', str(resp.content))
        self.assertIn('Test Account 1', str(resp.content))
        self.assertIn('Test Currency', str(resp.content))
        self.assertIn('0.00', str(resp.content))
        self.assertIn('Link', str(resp.content))

        self.assertIn('Test Bank 2', str(resp.content))
        self.assertIn('Test Account 2', str(resp.content))
