from django import forms

from transactions.models import Deposit, Withdrawal


class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = [
            'savings_account',
            'amount',
            'date',
            'income_source'
        ]


class WithdrawalForm(forms.ModelForm):
    class Meta:
        model = Withdrawal
        fields = [
            'savings_account',
            'amount',
            'date',
        ]
