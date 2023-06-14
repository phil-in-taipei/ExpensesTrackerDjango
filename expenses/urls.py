from django.urls import path

from .views import create_expense

app_name = 'expenses'
urlpatterns = [
    path('create-expense/', create_expense, name='create_income_source')
]