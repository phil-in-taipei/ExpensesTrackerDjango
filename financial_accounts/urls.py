from django.urls import path

from .views import create_savings_account, user_savings_accounts


app_name = 'financial_accounts'
urlpatterns = [
    path('create-savings-account/', create_savings_account, name='create_savings_account'),
    path('user-savings-accounts/', user_savings_accounts, name='user_savings_accounts'),
]
