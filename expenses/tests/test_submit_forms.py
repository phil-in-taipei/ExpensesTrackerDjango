from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from expenses.models import Expense

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
