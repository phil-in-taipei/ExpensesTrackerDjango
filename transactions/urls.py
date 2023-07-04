from django.urls import path

from transactions.views import account_transactions_searched_month, make_deposit, \
    delete_deposit, delete_withdrawal, make_withdrawal, \
    user_deposits_current_month, user_withdrawals_current_month, \
    user_withdrawals_searched_month, user_deposits_searched_month, \
    search_account_transactions_by_month_and_year, search_user_deposits_by_month_and_year, \
    search_user_withdrawals_by_month_and_year

app_name = 'transactions'
urlpatterns = [
    path('account-transactions-by-month/<int:month>/<int:year>/<int:savings_account_id>/',
         account_transactions_searched_month,
         name='account_transactions_searched_month'),
    path('delete-deposit/<int:id>/', delete_deposit, name='delete_deposit'),
    path('delete-withdrawal/<int:id>/', delete_withdrawal, name='delete_withdrawal'),
    path('make-deposit/', make_deposit, name='make_deposit'),
    path('make-withdrawal/', make_withdrawal, name='make_withdrawal'),
    path('search-account-transactions/', search_account_transactions_by_month_and_year,
         name='search_account_transactions_by_month_and_year'),
    path('search-user-deposits/', search_user_deposits_by_month_and_year,
         name='search_user_deposits_by_month_and_year'),
    path('search-user-withdrawals/', search_user_withdrawals_by_month_and_year,
         name='search_user_withdrawals_by_month_and_year'),
    path('user-deposits-current-month', user_deposits_current_month,
         name='user_deposits_current_month'),
    path('user-deposits-by-month/<int:month>/<int:year>/',
         user_deposits_searched_month,
         name='user_deposits_searched_month'),
    path('user-withdrawals-current-month', user_withdrawals_current_month,
         name='user_withdrawals_current_month'),
    path('user-withdrawals-by-month/<int:month>/<int:year>/',
         user_withdrawals_searched_month,
         name='user_withdrawals_searched_month'),
]
