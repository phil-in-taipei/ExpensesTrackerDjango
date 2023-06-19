from django.urls import path

from .views import create_expense, create_spending_record, \
    delete_expense,  update_expense, user_expenses, \
    user_expenditures_current_month

app_name = 'expenses'
urlpatterns = [
    path('create-expense/', create_expense, name='create_expense'),
    path('create-spending-record/', create_spending_record, name='create_spending_record'),
    path('delete-expense/<int:id>/', delete_expense, name='delete_expense'),
    path('update-expense/<int:id>/', update_expense, name='update_expense'),
    path('user-expenses/', user_expenses, name='user_expenses'),
    path('user-expenditures-by-month', user_expenditures_current_month,
         name='user_expenditures_current_month'),
]
