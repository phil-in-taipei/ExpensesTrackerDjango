#from django.test import TestCase
#from django.contrib.auth import get_user_model
#from django.urls import reverse

#from currencies.models import Currency
#from financial_accounts.models import Bank

#User = get_user_model()

"""
class CreateSavingsAccountViewPostTest(TestCase):
    #Test Create Savings Account View Form Submission
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
        resp = self.client.post(reverse('financial_accounts:create_savings_account'),
                                data={'bank': bank,
                                      'account_name': 'Test Savings Account',
                                      'currency': bank,
                                      },
                                content_type='application/x-www-form-urlencoded')

        self.assertEqual(resp.status_code, 302)
        print("This is the response:")
        print(resp.content)
         #redirects to user savings account page after submitting form data
        self.assertEqual(resp.url, reverse('financial_accounts:user_savings_accounts'))


"""

