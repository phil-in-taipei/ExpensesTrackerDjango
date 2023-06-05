from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from financial_accounts.forms import SavingsAccountForm
from financial_accounts.models import Bank, SavingsAccount


@login_required()
def create_savings_account(request):
    current_user = request.user
    if request.method == 'POST':
        form = SavingsAccountForm(request.POST or None)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.account_owner = current_user
            form_obj.save()
            return HttpResponseRedirect(reverse('financial_accounts:user_savings_accounts'))
    else:
        form = SavingsAccountForm()
    context = {
        "form": form,
        "user": current_user,
    }
    template = "financial_accounts/create-savings-account.html"
    return render(request, template, context)


@login_required()
def user_savings_accounts(request):
    current_user = request.user
    savings_accounts = SavingsAccount.objects.filter(account_owner=current_user)
    context = {
        "savings_accounts": savings_accounts,
        "user": current_user,
    }
    template = "financial_accounts/user-savings-accounts.html"
    return render(request, template, context)
