from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from financial_accounts.forms import SavingsAccountCreateForm, SavingsAccountUpdateForm
from financial_accounts.models import SavingsAccount


@login_required()
def create_savings_account(request):
    current_user = request.user
    if request.method == 'POST':
        form = SavingsAccountCreateForm(request.POST or None)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.account_owner = current_user
            form_obj.save()
            return HttpResponseRedirect(reverse('financial_accounts:user_savings_accounts'))
    else:
        form = SavingsAccountCreateForm()
    context = {
        "form": form,
        "user": current_user,
    }
    template = "financial_accounts/create-savings-account.html"
    return render(request, template, context)


@login_required()
def update_savings_account(request, id=None):
    current_user = request.user
    savings_account = get_object_or_404(SavingsAccount, id=id)
    if request.method == 'POST':
        form = SavingsAccountUpdateForm(request.POST or None, instance=savings_account)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.save()
            return HttpResponseRedirect(reverse('financial_accounts:user_savings_accounts'))
    else:
        form = SavingsAccountUpdateForm(instance=savings_account)
    context = {
        "user": current_user,
        "savings_account": savings_account,
        "form": form,
    }
    template = "financial_accounts/update-savings-account.html"
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
