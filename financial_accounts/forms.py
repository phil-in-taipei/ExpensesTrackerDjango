from django import forms
from .models import SavingsAccount, Bank


class SavingsAccountForm(forms.ModelForm):
    def __init__(self, *args,**kwargs):
        super(SavingsAccountForm, self).__init__(*args,**kwargs)
        self.fields['bank'].queryset = Bank.objects.all()

    class Meta:
        model = SavingsAccount
        fields = [
            'bank',
            'account_name',
            'currency',
        ]
