from django import forms
from .date_utilities import get_month_options_tuple

month_options = get_month_options_tuple()
year_options = Options = [
        (2023, '2023'),
        (2024, '2024'),
      ]


class SearchByMonthAndYearForm(forms.Form):
    month = forms.ChoiceField(label='Month', widget=forms.Select, choices=month_options)
    year = forms.ChoiceField(label='Year', widget=forms.Select, choices=year_options)