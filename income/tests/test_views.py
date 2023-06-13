from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from income.models import IncomeSource

User = get_user_model()


class IncomeViewsTest(TestCase):
    """Test Income Views"""

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username="TestUser1",
            password="testpassword"
        )
        self.client.force_login(self.user)
        self.test_income_source_1 = IncomeSource.objects.create(
            income_source_name="Test Income Source 1",
            user=self.user
        )
        self.test_income_source_2 = IncomeSource.objects.create(
            income_source_name="Test Income Source 2",
            user=self.user
        )

    def test_create_income_source(self):
        """Test Create Income Source View Form Display"""
        print("Test Create Income Source View Form Display")
        url = reverse('income:create_income_source')
        resp = self.client.get(url)
        #print(resp.content)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('Create Income Source', str(resp.content))
        self.assertIn('Income source name', str(resp.content))

    def test_update_income_source(self):
        """Test Update Income Source View Form Display"""
        print("Test Update Income Source View Form Display")
        url = reverse('income:update_income_source',
                      args=[self.test_income_source_1.id])
        resp = self.client.get(url)
        #print(resp.content)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('Update ' + str(self.test_income_source_1), str(resp.content))
        self.assertIn('Income source name', str(resp.content))

    def test_user_income_sources(self):
        """Test User's Income Sources List View Display"""
        print("Test User's Income Sources List View Display")
        url = reverse('income:user_income_sources')
        resp = self.client.get(url)
        #print(resp.content)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('TestUser1\\\'s Income Sources', str(resp.content))
        self.assertIn('Income Source Name', str(resp.content))
        self.assertIn('Edit', str(resp.content))
        self.assertIn('Delete', str(resp.content))

        self.assertIn('Test Income Source 1', str(resp.content))
        self.assertIn('Link', str(resp.content))
        self.assertIn('Remove', str(resp.content))

        self.assertIn('Test Income Source 2', str(resp.content))

