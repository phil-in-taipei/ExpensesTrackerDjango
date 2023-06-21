import datetime
from dateutil.relativedelta import relativedelta
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from currencies.models import Currency
from expenses.models import Expense, SpendingRecord
from utilities.date_utilities import get_name_of_current_month, get_list_of_months

User = get_user_model()


class ExpensesViewsTest(TestCase):
    """Test Expenses Views"""

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username="TestUser1",
            password="testpassword"
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

        self.test_expense_2 = Expense.objects.create(
            expense_name="Test Expense 2",
            user=self.user
        )

        self.test_expense_3 = Expense.objects.create(
            expense_name="Test Expense 3",
            user=self.user
        )

        self.today = datetime.date.today()
        self.first_day_of_this_month = datetime.date(self.today.year, self.today.month, 1)
        self.first_day_of_next_month = self.first_day_of_this_month + relativedelta(months=1)
        self.last_day_of_this_month = self.first_day_of_next_month - relativedelta(days=1)
        self.current_month_str = get_name_of_current_month()

        self.test_spending_record_1 = SpendingRecord.objects.create(
            amount=100.00,
            date=self.first_day_of_this_month,
            expense=self.test_expense_1,
            currency=self.currency
        )

        self.test_spending_record_2 = SpendingRecord.objects.create(
            amount=1200.00,
            date=self.last_day_of_this_month,
            expense=self.test_expense_2,
            currency=self.currency
        )

        self.test_spending_record_3 = SpendingRecord.objects.create(
            amount=100.00,
            date=self.first_day_of_next_month,
            expense=self.test_expense_3,
            currency=self.currency
        )

    def test_create_expense(self):
        """Test Create Expense View Form Display"""
        print("Test Expense Source View Form Display")
        url = reverse('expenses:create_expense')
        resp = self.client.get(url)
        #print(resp.content)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('Create Expense', str(resp.content))
        self.assertIn('Expense name', str(resp.content))

    def test_create_spending_record(self):
        """Test Create Spending Record View Form Display"""
        print("Test Spending Record View Form Display")
        url = reverse('expenses:create_spending_record')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('Create Spending Record', str(resp.content))
        self.assertIn('Expense', str(resp.content))
        self.assertIn('Amount', str(resp.content))
        self.assertIn('Date', str(resp.content))
        self.assertIn('Currency', str(resp.content))

    def test_search_user_expenditures_by_month_and_year(self):
        """Test Search User Spending Record By Month/Year View Form Display"""
        print("Test Search User Spending Record By Month/Year View Form Display")
        url = reverse('expenses:search_user_expenditures_by_month_and_year')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('Search Spending Records', str(resp.content))
        month_list = get_list_of_months()
        for month in month_list:
            self.assertIn(month, str(resp.content))
        self.assertIn('2023', str(resp.content))
        self.assertIn('2024', str(resp.content))

    def test_update_expense(self):
        """Test Update Expense View Form Display"""
        print("Test Expense View Form Display")
        url = reverse('expenses:update_expense',
                      args=[self.test_expense_1.id])
        resp = self.client.get(url)
        #print(resp.content)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('Update ' + str(self.test_expense_1), str(resp.content))
        self.assertIn('Expense name', str(resp.content))

    def test_user_expenses(self):
        """Test User's Expenses List View Display"""
        print("Test User's Expenses List View Display")
        url = reverse('expenses:user_expenses')
        resp = self.client.get(url)
        #print(resp.content)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('TestUser1\\\'s Expenses', str(resp.content))
        self.assertIn('Expense Name', str(resp.content))
        self.assertIn('Edit', str(resp.content))
        self.assertIn('Delete', str(resp.content))

        self.assertIn('Test Expense 1', str(resp.content))
        self.assertIn('Link', str(resp.content))
        self.assertIn('Remove', str(resp.content))

        self.assertIn('Test Expense 2', str(resp.content))

    def test_user_expenditures_current_month(self):
        """Test User's Expenditures List View (current month) Display"""
        print("Test User's Expenditures List View (current month) Display")
        url = reverse('expenses:user_expenditures_current_month')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('TestUser1\\\'s Spending Records', str(resp.content))
        self.assertIn(self.current_month_str, str(resp.content))
        self.assertIn(str(self.today.year), str(resp.content))
        self.assertIn('Name', str(resp.content))
        self.assertIn('Date', str(resp.content))
        self.assertIn('Amount', str(resp.content))
        self.assertIn('Currency', str(resp.content))

        self.assertIn('Test Expense 1', str(resp.content))
        self.assertIn('100.00', str(resp.content))
        self.assertIn('Test Currency', str(resp.content))

        self.assertIn('Test Expense 2', str(resp.content))
        self.assertIn('1200.00', str(resp.content))

        self.assertIn('1200.00', str(resp.content))
        self.assertNotIn('Test Expense 3',  str(resp.content))

    def test_user_expenditures_searched_month(self):
        """Test User's Expenditures List View (searched month/year) Display"""
        print("Test User's Expenditures List View (searched month/year) Display")
        url = reverse('expenses:user_expenditures_searched_month',
                      kwargs={'month': self.today.month, 'year': self.today.year})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('TestUser1\\\'s Spending Records', str(resp.content))
        self.assertIn(self.current_month_str, str(resp.content))
        self.assertIn(str(self.today.year), str(resp.content))
        self.assertIn('Name', str(resp.content))
        self.assertIn('Date', str(resp.content))
        self.assertIn('Amount', str(resp.content))
        self.assertIn('Currency', str(resp.content))

        self.assertIn('Test Expense 1', str(resp.content))
        self.assertIn('100.00', str(resp.content))
        self.assertIn('Test Currency', str(resp.content))

        self.assertIn('Test Expense 2', str(resp.content))
        self.assertIn('1200.00', str(resp.content))

        self.assertIn('1200.00', str(resp.content))
        self.assertNotIn('Test Expense 3',  str(resp.content))