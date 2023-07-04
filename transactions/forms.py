from django import forms

from financial_accounts.models import SavingsAccount
from transactions.models import Deposit, Withdrawal
from utilities.date_utilities import get_month_options_tuple
from utilities.search_by_month_and_year_form import SearchByMonthAndYearForm


class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = [
            'savings_account',
            'amount',
            'date',
            'income_source'
        ]


month_options = get_month_options_tuple()
year_options = [
        (2023, '2023'),
        (2024, '2024'),
      ]
savings_account_options = []


class SearchByAccountAndMonthAndYearForm(forms.Form):
    savings_account = forms.ChoiceField(label='Savings Account', widget=forms.Select,
                                        choices=savings_account_options)
    month = forms.ChoiceField(label='Month', widget=forms.Select, choices=month_options)
    year = forms.ChoiceField(label='Year', widget=forms.Select, choices=year_options)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.user = user
        user_savings_accounts = SavingsAccount.objects.filter(account_owner=self.user)
        savings_account_options_list = []
        for i in range(len(user_savings_accounts)):
            option_tuple = (user_savings_accounts[i].pk, user_savings_accounts[i])
            savings_account_options_list.append(option_tuple)
        savings_account_options_tuple = tuple(savings_account_options_list)
        self.fields['savings_account'].choices = savings_account_options_tuple


class WithdrawalForm(forms.ModelForm):
    class Meta:
        model = Withdrawal
        fields = [
            'savings_account',
            'amount',
            'date',
        ]
