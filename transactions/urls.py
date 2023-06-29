from django.urls import path

from transactions.views import make_deposit, \
    user_deposits_current_month, \
    make_withdrawal, user_withdrawals_current_month, \
    user_withdrawals_searched_month, user_deposits_searched_month, \
    search_user_deposits_by_month_and_year, \
    search_user_withdrawals_by_month_and_year

app_name = 'transactions'
urlpatterns = [
    path('make-deposit/', make_deposit, name='make_deposit'),
    path('make-withdrawal/', make_withdrawal, name='make_withdrawal'),
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
