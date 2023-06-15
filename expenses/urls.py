from django.urls import path

from .views import create_expense, delete_expense,  update_expense, user_expenses

app_name = 'expenses'
urlpatterns = [
    path('create-expense/', create_expense, name='create_expense'),
    path('delete-expense/<int:id>/', delete_expense, name='delete_expense'),
    path('update-expense/<int:id>/', update_expense, name='update_expense'),
    path('user-expenses/', user_expenses, name='user_expenses')
]
