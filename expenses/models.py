import datetime
from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _

from currencies.models import Currency


class Expense(models.Model):
    expense_name = models.CharField(max_length=250)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ('user', 'expense_name')

    def __str__(self):
        return "{}: {}".format(
            self.user,
            self.expense_name
        ).title()


class SpendingRecord(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE,
                                 null=True, blank=True)
    date = models.DateField(_("Date"), default=datetime.date.today)
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE,
                                null=True, blank=True)

    def __str__(self):
        return "{} | {} | Amount: {}".format(
            self.expense,
            self.date,
            self.amount,
        ).title()
