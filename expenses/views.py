import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from expenses.forms import ExpenseForm, SpendingRecordForm
from expenses.models import Expense, SpendingRecord

from utilities.date_utilities import get_list_of_months, \
    get_name_of_current_month


@login_required()
def create_expense(request):
    current_user = request.user
    if request.method == 'POST':
        form = ExpenseForm(request.POST or None)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.user = current_user
            form_obj.save()
            return HttpResponseRedirect(reverse('expenses:user_expenses'))
    else:
        form = ExpenseForm()
    context = {
        "form": form,
        "user": current_user,
    }
    template = "expenses/create-expense.html"
    return render(request, template, context)


@login_required()
def create_spending_record(request):
    current_user = request.user
    if request.method == 'POST':
        form = SpendingRecordForm(request.POST or None)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.user = current_user
            form_obj.save()
            return HttpResponseRedirect(reverse(
                'expenses:user_expenditures_current_month')
            )
    else:
        form = SpendingRecordForm()
    context = {
        "form": form,
        "user": current_user,
    }
    template = "expenses/create-spending-record.html"
    return render(request, template, context)


@login_required()
def delete_expense(request, id=None):
    expense = get_object_or_404(Expense, id=id)
    if expense:
        expense.delete()
    return HttpResponseRedirect(reverse('expenses:user_expenses'))


@login_required()
def update_expense(request, id=None):
    current_user = request.user
    expense = get_object_or_404(Expense, id=id)
    if request.method == 'POST':
        form = ExpenseForm(request.POST or None, instance=expense)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.user = current_user
            form_obj.save()
            return HttpResponseRedirect(reverse('expenses:user_expenses'))
    else:
        form = ExpenseForm(instance=expense)
    context = {
        "expense": expense,
        "form": form,
        "user": current_user,
    }
    template = "expenses/update-expense.html"
    return render(request, template, context)


@login_required()
def user_expenses(request):
    current_user = request.user
    expenses = Expense.objects.filter(user=current_user)
    context = {
        "expenses": expenses,
        "user": current_user
    }
    template = "expenses/user-expenses.html"
    return render(request, template, context)


@login_required()
def user_expenditures_current_month(request):
    current_user = request.user
    month = get_name_of_current_month()
    year = datetime.date.today().year
    spending_records = SpendingRecord.custom_query\
        .users_spending_records_for_current_month(user=current_user)
    context = {
        "month": month,
        "spending_records": spending_records,
        "user": current_user,
        "year": year,
    }
    template = "expenses/user-spending-records-by-month.html"
    return render(request, template, context)
