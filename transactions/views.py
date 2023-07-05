import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from financial_accounts.models import SavingsAccount
from transactions.forms import DepositForm, WithdrawalForm, SearchByAccountAndMonthAndYearForm
from transactions.models import Deposit, Withdrawal
from utilities.date_utilities import get_name_of_current_month, get_name_of_month_by_number
from utilities.search_by_month_and_year_form import SearchByMonthAndYearForm


# this function will render a list of all transactions
# (Deposits and Withdrawals mixed data types), for a given
# SavingsAccount in a given month/year, sorted by date
@login_required()
def account_transactions_searched_month(
        request, month=None, year=None, savings_account_id=None
    ):
    current_user = request.user
    savings_account = get_object_or_404(
        SavingsAccount, id=savings_account_id
    )
    # this will be used to collect a list of tuples containing
    # a transaction object (either a Deposit or a Withdrawal)
    # and the date of the transaction
    transactions_by_date_tuple_list = []
    deposits = Deposit.custom_query\
        .account_deposits_for_queried_month_and_year(
            savings_account_id=savings_account_id, month=month, year=year
        )
    for i in range(len(deposits)):
        # tuple with three indexes -- one of the date, and
        # the other of the deposit object, and the third is
        # a string specifying that it is a 'Deposit'
        deposit_by_date_tuple = (deposits[i].date, (deposits[i], 'Deposit'))
        transactions_by_date_tuple_list.append(deposit_by_date_tuple)
    withdrawals = Withdrawal.custom_query\
        .account_withdrawals_for_queried_month_and_year(
            savings_account_id=savings_account_id, month=month, year=year
        )
    for i in range(len(withdrawals)):
        # tuple with two indexes -- one of the date, and the
        # other of the  withdrawal object, and the third is
        # a string specifying that it is a 'Withdrawal'
        withdrawal_by_date_tuple = (withdrawals[i].date, (withdrawals[i], 'Withdrawal'))
        transactions_by_date_tuple_list.append(withdrawal_by_date_tuple)
    # the transaction tuples are sorted by date, and then a list of the 2nd two
    # indexes will be added into the template context --
    # transaction object, and transaction type string
    transactions = sorted(transactions_by_date_tuple_list, key=lambda x: x[0])
    context = {
        "month": get_name_of_month_by_number(month),
        'savings_account': savings_account,
        "transactions": [transaction[1] for transaction in transactions],
        "user": current_user,
        "year": year,
    }
    template = "transactions/account-transactions-by-month-and-year.html"
    return render(request, template, context)


@login_required()
def delete_deposit(request, id=None):
    deposit = get_object_or_404(Deposit, id=id)
    if deposit:
        amount = deposit.amount
        savings_account = deposit.savings_account
        deposit.delete()
        savings_account.account_balance -= amount
        savings_account.save()
    return HttpResponseRedirect(reverse('transactions:user_deposits_current_month'))


@login_required()
def delete_withdrawal(request, id=None):
    withdrawal = get_object_or_404(Withdrawal, id=id)
    if withdrawal:
        amount = withdrawal.amount
        savings_account = withdrawal.savings_account
        withdrawal.delete()
        savings_account.account_balance += amount
        savings_account.save()
    return HttpResponseRedirect(reverse('transactions:user_withdrawals_current_month'))


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
def search_account_transactions_by_month_and_year(request):
    if request.method == "POST":
        form = SearchByAccountAndMonthAndYearForm(request.POST, user=request.user)
        if form.is_valid():
            month = form.cleaned_data["month"]
            year = form.cleaned_data["year"]
            savings_account = form.cleaned_data["savings_account"]
            return HttpResponseRedirect(
                reverse('transactions:account_transactions_searched_month',
                        kwargs={'month': month, 'year': year,
                                'savings_account_id': savings_account}))
    else:
        form = SearchByAccountAndMonthAndYearForm(user=request.user)
    template = 'transactions/search-account-transactions-by-month-and-year.html'
    context = {"form": form}
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
