import datetime
from django.test import TestCase

from utilities.search_by_month_and_year_form import SearchByMonthAndYearForm

today = datetime.date.today()


class SearchByMonthAndYearFormTests(TestCase):
    """Test the Search By Month and Year Form"""

    def test_valid_form(self):
        print("Test that the Search by Month and Year Form is Valid")
        data = {
            'month': today.month,
            'year': today.year,
        }
        form = SearchByMonthAndYearForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        print("Test that the Search by Month and Year Form is Invalid")
        data = {
            'month': 'lahhalahhdlksalkdsahdsads',
            'year': today.year,
        }
        form = SearchByMonthAndYearForm(data=data)
        self.assertFalse(form.is_valid())
