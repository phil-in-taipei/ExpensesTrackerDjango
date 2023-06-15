from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from expenses.models import Expense

User = get_user_model()


class ExpensesViewsTest(TestCase):
    """Test Expenses Views"""

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username="TestUser1",
            password="testpassword"
        )
        self.client.force_login(self.user)

        self.test_expense_1 = Expense.objects.create(
            expense_name="Test Expense 1",
            user=self.user
        )

        self.test_expense_2 = Expense.objects.create(
            expense_name="Test Expense 2",
            user=self.user
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

