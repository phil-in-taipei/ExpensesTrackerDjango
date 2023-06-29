import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from transactions.forms import DepositForm, WithdrawalForm
from transactions.models import Deposit, Withdrawal
from utilities.date_utilities import get_name_of_current_month, get_name_of_month_by_number
from utilities.search_by_month_and_year_form import SearchByMonthAndYearForm


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
def search_user_deposits_by_month_and_year(request):
    if request.method == "POST":
        form = SearchByMonthAndYearForm(request.POST)
        if form.is_valid():
            month = form.cleaned_data["month"]
            year = form.cleaned_data["year"]
            return HttpResponseRedirect(
                reverse('transactions:user_deposits_searched_month',
                        kwargs={'month': month, 'year': year}))
    else:
        form = SearchByMonthAndYearForm()
    template = 'transactions/search-deposits-by-month-and-year.html'
    context = {"form": form}
    return render(request, template, context)


@login_required()
def search_user_withdrawals_by_month_and_year(request):
    if request.method == "POST":
        form = SearchByMonthAndYearForm(request.POST)
        if form.is_valid():
            month = form.cleaned_data["month"]
            year = form.cleaned_data["year"]
            return HttpResponseRedirect(
                reverse('transactions:user_withdrawals_searched_month',
                        kwargs={'month': month, 'year': year}))
    else:
        form = SearchByMonthAndYearForm()
    template = 'transactions/search-withdrawals-by-month-and-year.html'
    context = {"form": form}
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
def user_deposits_searched_month(request, month=None, year=None):
    current_user = request.user
    deposits = Deposit.custom_query\
        .users_deposits_for_queried_month_and_year(
            user=current_user, month=month, year=year
        )
    context = {
        "month": get_name_of_month_by_number(month),
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


@login_required()
def user_withdrawals_searched_month(request, month=None, year=None):
    current_user = request.user
    withdrawals = Withdrawal.custom_query\
        .users_withdrawals_for_queried_month_and_year(
            user=current_user, month=month, year=year
        )
    context = {
        "month": get_name_of_month_by_number(month),
        "withdrawals": withdrawals,
        "user": current_user,
        "year": year,
    }
    template = "transactions/user-withdrawals-by-month.html"
    return render(request, template, context)
