from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .forms import IncomeSourceForm
from .models import IncomeSource


@login_required()
def create_income_source(request):
    current_user = request.user
    if request.method == 'POST':
        form = IncomeSourceForm(request.POST or None)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.user = current_user
            form_obj.save()
            return HttpResponseRedirect(reverse('income:user_income_sources'))
    else:
        form = IncomeSourceForm()
    context = {
        "form": form,
        "user": current_user,
    }
    template = "income/create-income-source.html"
    return render(request, template, context)


@login_required()
def delete_income_source(request, id=None):
    income_source = get_object_or_404(IncomeSource, id=id)
    if income_source:
        income_source.delete()
    return HttpResponseRedirect(reverse('income:user_income_sources'))


@login_required()
def update_income_source(request, id=None):
    current_user = request.user
    income_source = get_object_or_404(IncomeSource, id=id)
    if request.method == 'POST':
        form = IncomeSourceForm(request.POST or None, instance=income_source)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.user = current_user
            form_obj.save()
            return HttpResponseRedirect(reverse('income:user_income_sources'))
    else:
        form = IncomeSourceForm(instance=income_source)
    context = {
        "form": form,
        "income_source": income_source,
        "user": current_user,
    }
    template = "income/update-income-source.html"
    return render(request, template, context)


@login_required()
def user_income_sources(request):
    current_user = request.user
    income_sources = IncomeSource.objects.filter(user=current_user)
    context = {
        "income_sources": income_sources,
        "user": current_user,
    }
    template = "income/user-income-sources.html"
    return render(request, template, context)

