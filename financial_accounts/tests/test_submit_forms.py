from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from currencies.models import Currency
from financial_accounts.models import Bank, SavingsAccount

User = get_user_model()


class CreateSavingsAccountViewPostTest(TestCase):
    """Test Create Savings Account View Form Submission"""
    def setUp(self):
        self.user = User.objects.create_user(
            'testuser',
            'testpassword'
        )
        self.client.force_login(self.user)

    def test_create_savings_account_post(self):
        print("Test Create Savings Account View Form Post")
        bank = Bank.objects.create(bank_name="Test Bank")
        bank.save()
        currency = Currency.objects.create(
            currency_name="Test Currency",
            currency_code="TRY"
        )
        currency.save()
        data = {'bank': str(bank.pk),
                'account_name': 'Test Savings Account',
                'currency': str(currency.pk),
                }
        resp = self.client.post(reverse('financial_accounts:create_savings_account'),
                                data=data)
        self.assertEqual(resp.status_code, 302)
         #redirects to user savings account page after submitting form data
        self.assertEqual(resp.url, reverse('financial_accounts:user_savings_accounts'))


class UpdateSavingsAccountPostTest(TestCase):
    """Test Update Savings Account View Form Submission"""
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
        self.savings_account = SavingsAccount.objects.create(
            account_owner=self.user,
            bank=self.bank,
            account_name='Test Savings Account',
            currency=self.currency,
        )

    def test_update_savings_account_post(self):
        print("Test Update Savings Account View Form Post")

        data = {
                'account_name': 'Test Savings Account Revised',
                'account_balance': 100.00,
                }
        resp = self.client.post(reverse('financial_accounts:update_savings_account'
                                , kwargs={'id': self.savings_account.id}),
                                data=data)
        self.assertEqual(resp.status_code, 302)
         #redirects to user savings account page after submitting form data
        self.assertEqual(resp.url, reverse('financial_accounts:user_savings_accounts'))
