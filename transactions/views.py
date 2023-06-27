import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from transactions.forms import DepositForm, WithdrawalForm
from transactions.models import Deposit, Withdrawal
from utilities.date_utilities import get_name_of_current_month


@login_required()
def make_deposit(request):
    current_user = request.user
    if request.method == 'POST':
        form = DepositForm(request.POST or None)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.user = current_user
            form_obj.save()
            savings_account = form_obj.savings_account
            savings_account.account_balance += form_obj.amount
            savings_account.save()
        return HttpResponseRedirect(reverse('transactions:user_deposits_current_month'))
    else:
        form = DepositForm
    context = {
        "form": form,
        "user": current_user,
    }
    template = "transactions/make-deposit.html"
    return render(request, template, context)


@login_required()
def make_withdrawal(request):
    current_user = request.user
    if request.method == 'POST':
        form = WithdrawalForm(request.POST or None)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.user = current_user
            form_obj.save()
            savings_account = form_obj.savings_account
            savings_account.account_balance -= form_obj.amount
            savings_account.save()
        return HttpResponseRedirect(reverse('transactions:user_withdrawals_current_month'))
    else:
        form = WithdrawalForm
    context = {
        "form": form,
        "user": current_user,
    }
    template = "transactions/make-withdrawal.html"
    return render(request, template, context)


@login_required()
def user_deposits_current_month(request):
    current_user = request.user
    month = get_name_of_current_month()
    year = datetime.date.today().year
    deposits = Deposit.custom_query\
        .users_deposits_for_current_month(user=current_user)
    context = {
        "month": month,
        "deposits": deposits,
        "user": current_user,
        "year": year,
    }
    template = "transactions/user-deposits-by-month.html"
    return render(request, template, context)


@login_required()
def user_withdrawals_current_month(request):
    current_user = request.user
    month = get_name_of_current_month()
    year = datetime.date.today().year
    withdrawals = Withdrawal.custom_query\
        .users_withdrawals_for_current_month(user=current_user)
    context = {
        "month": month,
        "withdrawals": withdrawals,
        "user": current_user,
        "year": year,
    }
    template = "transactions/user-withdrawals-by-month.html"
    return render(request, template, context)
