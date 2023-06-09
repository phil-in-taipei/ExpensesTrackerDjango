from django import forms

from currencies.models import Currency
from .models import SavingsAccount, Bank


class SavingsAccountCreateForm(forms.ModelForm):
    #def __init__(self, *args,**kwargs):
    #    super(SavingsAccountForm, self).__init__(*args, **kwargs)
    #    self.fields['bank'].queryset = Bank.objects.all()
    #    self.fields['currency'].queryset = Currency.objects.all()

    class Meta:
        model = SavingsAccount
        fields = [
            'bank',
            'account_name',
            'currency',
        ]


class SavingsAccountUpdateForm(forms.ModelForm):
    class Meta:
        model = SavingsAccount
        fields = [
            'account_name',
            'account_balance',
        ]
