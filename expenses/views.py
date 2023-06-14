from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required()
def create_expense(request):
    current_user = request.user
    #if request.method == 'POST':
    #    form = IncomeSourceForm(request.POST or None)
    #    if form.is_valid():
    #        form_obj = form.save(commit=False)
    #        form_obj.user = current_user
    #        form_obj.save()
    #        return HttpResponseRedirect(reverse('income:user_income_sources'))
    #else:
    #    form = IncomeSourceForm()
    context = {
     #   "form": form,
        "user": current_user,
    }
    template = "expenses/create-expense.html"
    return render(request, template, context)

