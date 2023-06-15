from django import forms
from .models import Expense, SpendingRecord


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = [
            'expense_name',
        ]


class SpendingRecordForm(forms.ModelForm):
    class Meta:
        model = SpendingRecord
        fields = [
            'expense',
            'currency',
            'amount',
            'date'
        ]
