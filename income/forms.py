from django import forms
from income.models import IncomeSource


class IncomeSourceForm(forms.ModelForm):
    class Meta:
        model = IncomeSource
        fields = [
            'income_source_name',
        ]
