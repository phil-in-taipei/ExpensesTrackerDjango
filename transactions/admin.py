from django.contrib import admin
from transactions.models import Deposit, Withdrawal

admin.site.register(Deposit)
admin.site.register(Withdrawal)
