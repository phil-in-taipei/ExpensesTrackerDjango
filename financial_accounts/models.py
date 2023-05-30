from django.db import models
from django.conf import settings

from currencies.models import Currency


class Bank(models.Model):
    bank_name = models.CharField(max_length=200)

    def __str__(self):
        return self.bank_name


class SavingsAccount(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=300)
    account_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    account_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "{}: {} Account ({})".format(
            self.account_owner,
            self.bank,
            self.account_name
        )
