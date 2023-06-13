from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from income.models import IncomeSource

User = get_user_model()


class CreateIncomeViewPostTest(TestCase):
    """Test Create Income Source View Form Submission"""
    def setUp(self):
        self.user = User.objects.create_user(
            'testuser',
            'testpassword'
        )
        self.client.force_login(self.user)

    def test_create_income_source_post(self):
        print("Test Create Income Source View Form Post")
        data = {'income_source_name': 'Test Income Source'}
        resp = self.client.post(reverse('income:create_income_source'),
                                data=data)
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.url, reverse('income:user_income_sources'))


class DeleteIncomeViewPostTest(TestCase):
    """Test Delete Income Source View"""
    def setUp(self):
        self.user = User.objects.create_user(
            'testuser',
            'testpassword'
        )
        self.client.force_login(self.user)
        self.income_source = IncomeSource.objects.create(
            income_source_name="Test Income Source",
            user=self.user
        )

    def test_delete_income_source_post(self):
        print("Test Delete Income Source View Form Post")
        deleted_id = self.income_source.id
        resp = self.client.post(reverse('income:delete_income_source'
                                , kwargs={'id': deleted_id}))
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.url, reverse('income:user_income_sources'))
        with self.assertRaises(IncomeSource.DoesNotExist):
            IncomeSource.objects.get(id=deleted_id)


class UpdateIncomeViewPostTest(TestCase):
    """Test Update Income Source View Form Submission"""
    def setUp(self):
        self.user = User.objects.create_user(
            'testuser',
            'testpassword'
        )
        self.client.force_login(self.user)
        self.income_source = IncomeSource.objects.create(
            income_source_name="Test Income Source",
            user=self.user
        )

    def test_update_income_source_post(self):
        print("Test Update Income Source View Form Post")

        data = {'income_source_name': 'Test Income Source Revision'}
        resp = self.client.post(reverse('income:update_income_source'
                                , kwargs={'id': self.income_source.id}),
                                data=data)
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.url, reverse('income:user_income_sources'))
        self.assertEqual(
            IncomeSource.objects.get(id=self.income_source.id).income_source_name,
            'Test Income Source Revision'
        )
