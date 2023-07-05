from django import forms

from financial_accounts.models import SavingsAccount
from transactions.models import Deposit, Withdrawal
#from utilities.date_utilities import get_month_options_tuple
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


# this inherits from the SearchByMonthAndYearForm and adds another field
# to search for savings account. In the overridden __init__, it allows
# for the user to be passed in as a kwarg so that all of the user's
# savings accounts can be queried and then inserted into a nested tuple
# with each SavingsAccount object in a tuple with it's pk as a template selector
class SearchByAccountAndMonthAndYearForm(SearchByMonthAndYearForm):
    savings_account = forms.ChoiceField(label='Savings Account', widget=forms.Select,
                                        choices=())

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
