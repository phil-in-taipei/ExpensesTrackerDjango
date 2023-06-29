from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from currencies.models import Currency
from expenses.models import Expense, SpendingRecord

User = get_user_model()


class CreateExpenseViewPostTest(TestCase):
    """Test Create Expense View Form Submission"""
    def setUp(self):
        self.user = User.objects.create_user(
            'testuser',
            'testpassword'
        )
        self.client.force_login(self.user)

    def test_create_expense_post(self):
        print("Test Create Expense View Form Post")
        data = {'expense_name': 'Test Expense 1'}
        resp = self.client.post(reverse('expenses:create_expense'),
                                data=data)
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.url, reverse('expenses:user_expenses'))


class CreateSpendingRecordViewPostTest(TestCase):
    """Test Create Spending Record View Form Submission"""
    def setUp(self):
        self.user = User.objects.create_user(
            'testuser',
            'testpassword'
        )
        self.client.force_login(self.user)

        self.currency = Currency.objects.create(
            currency_name="Test Currency",
            currency_code="TRY"
        )

        self.test_expense_1 = Expense.objects.create(
            expense_name="Test Expense 1",
            user=self.user
        )

    def test_create_spending_record_post(self):
        print("Test Create Spending Record View Form Post")
        today = datetime.today()
        today_str = F"{today.year}-{today.month}-{today.day}"
        data = {
            'date': today_str,
            'currency': str(self.currency.pk),
            'expense': str(self.test_expense_1.pk),
            'amount': 100.00
        }
        resp = self.client.post(reverse('expenses:create_spending_record'),
                                data=data)
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.url, reverse('expenses:user_expenditures_current_month'))


class DeleteExpenseViewPostTest(TestCase):
    """Test Delete Expense View"""
    def setUp(self):
        self.user = User.objects.create_user(
            'testuser',
            'testpassword'
        )
        self.client.force_login(self.user)
        self.expense = Expense.objects.create(
            expense_name="Test Expense 1",
            user=self.user
        )

    def test_delete_expense_post(self):
        print("Test Delete Expense View Form Post")
        deleted_id = self.expense.id
        resp = self.client.post(reverse('expenses:delete_expense'
                                , kwargs={'id': deleted_id}))
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.url, reverse('expenses:user_expenses'))
        with self.assertRaises(Expense.DoesNotExist):
            Expense.objects.get(id=deleted_id)


class DeleteSpendingRecordViewPostTest(TestCase):
    """Test Delete Spending Record View"""
    def setUp(self):
        self.user = User.objects.create_user(
            'testuser',
            'testpassword'
        )
        self.client.force_login(self.user)
        self.currency = Currency.objects.create(
            currency_name="Test Currency",
            currency_code="TRY"
        )
        self.expense = Expense.objects.create(
            expense_name="Test Expense 1",
            user=self.user
        )
        self.spending_record = SpendingRecord.objects.create(
            amount=500.00,
            currency=self.currency,
            date=datetime.today(),
            expense=self.expense
        )

    def test_delete_spending_record_post(self):
        print("Test Delete Spending Record View Form Post")
        deleted_id = self.spending_record.id
        resp = self.client.post(reverse('expenses:delete_spending_record'
                                , kwargs={'id': deleted_id}))
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.url, reverse('expenses:user_expenditures_current_month'))
        with self.assertRaises(SpendingRecord.DoesNotExist):
            SpendingRecord.objects.get(id=deleted_id)


class SearchUserExpendituresViewPostTest(TestCase):
    """Test Search User Expenditures (month/year) View Form Submission"""
    def setUp(self):
        self.user = User.objects.create_user(
            'testuser',
            'testpassword'
        )
        self.client.force_login(self.user)

    def test_search_user_expenditures_post(self):
        print("Test Search User Expenditures (month/year) View Form Post")
        today = datetime.today()
        data = {
            'month': today.month,
            'year': today.year,
        }
        resp = self.client.post(reverse(
            'expenses:search_user_expenditures_by_month_and_year'),
             data=data)
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.url, reverse(
            'expenses:user_expenditures_searched_month',
            kwargs={'month': today.month, 'year': today.year}))


class UpdateExpensePostTest(TestCase):
    """Test Update Expense View Form Submission"""
    def setUp(self):
        self.user = User.objects.create_user(
            'testuser',
            'testpassword'
        )
        self.client.force_login(self.user)
        self.expense = Expense.objects.create(
            expense_name="Test Expense 1",
            user=self.user
        )

    def test_update_expense_post(self):
        print("Test Update Expense View Form Post")

        data = {'expense_name': 'Test Expense 1 Revision'}
        resp = self.client.post(reverse('expenses:update_expense'
                                , kwargs={'id': self.expense.id}),
                                data=data)
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.url, reverse('expenses:user_expenses'))
        self.assertEqual(
            Expense.objects.get(id=self.expense.id).expense_name,
            'Test Expense 1 Revision'
        )
