from django.urls import path

from transactions.views import make_deposit, \
    user_deposits_current_month, \
    make_withdrawal, \
    user_withdrawals_current_month

app_name = 'transactions'
urlpatterns = [
    path('make-deposit/', make_deposit, name='make_deposit'),
    path('make-withdrawal/', make_withdrawal, name='make_withdrawal'),
    path('user-deposits-current-month', user_deposits_current_month,
         name='user_deposits_current_month'),
    path('user-withdrawals-current-month', user_withdrawals_current_month,
         name='user_withdrawals_current_month')
]
