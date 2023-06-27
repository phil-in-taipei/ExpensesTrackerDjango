import datetime
from dateutil.relativedelta import relativedelta
from django.db import models
from django.utils.translation import gettext as _

from financial_accounts.models import SavingsAccount
from income.models import IncomeSource


class DepositManager(models.Manager):
    def users_deposits_for_current_month(self, user):
        today = datetime.date.today()
        first_day_of_this_month = datetime.date(today.year, today.month, 1)
        first_day_of_next_month = first_day_of_this_month + relativedelta(months=1)
        last_day_of_this_month = first_day_of_next_month - relativedelta(days=1)
        spending_records = self.get_queryset().filter(
            savings_account__user=user,
            date__gte=first_day_of_this_month,
            date__lte=last_day_of_this_month
        )
        return spending_records

    def users_deposits_for_queried_month_and_year(self, user, month, year):
        first_day_of_queried_month = datetime.date(year, month, 1)
        first_day_of_the_following_month = first_day_of_queried_month + relativedelta(months=1)
        last_day_of_the_queried_month = first_day_of_the_following_month - relativedelta(days=1)
        spending_records = self.get_queryset().filter(
            savings_account__user=user,
            date__gte=first_day_of_queried_month,
            date__lte=last_day_of_the_queried_month
        )
        return spending_records


class Deposit(models.Model):
    custom_query = DepositManager()
    objects = models.Manager()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(_("Date"), default=datetime.date.today)
    income_source = models.ForeignKey(IncomeSource, on_delete=models.CASCADE,
                                      null=True, blank=True)
    savings_account = models.ForeignKey(SavingsAccount, on_delete=models.CASCADE,
                                        null=True, blank=True)

    class Meta:
        ordering = ('savings_account', 'date')

    def __str__(self):
        return "{} | {} | Amount: {}".format(
            self.date,
            str(self.savings_account),
            self.amount,
        ).title()


class WithdrawalManager(models.Manager):
    def users_withdrawals_for_current_month(self, user):
        today = datetime.date.today()
        first_day_of_this_month = datetime.date(today.year, today.month, 1)
        first_day_of_next_month = first_day_of_this_month + relativedelta(months=1)
        last_day_of_this_month = first_day_of_next_month - relativedelta(days=1)
        spending_records = self.get_queryset().filter(
            savings_account__user=user,
            date__gte=first_day_of_this_month,
            date__lte=last_day_of_this_month
        )
        return spending_records

    def users_withdrawals_for_queried_month_and_year(self, user, month, year):
        first_day_of_queried_month = datetime.date(year, month, 1)
        first_day_of_the_following_month = first_day_of_queried_month + relativedelta(months=1)
        last_day_of_the_queried_month = first_day_of_the_following_month - relativedelta(days=1)
        spending_records = self.get_queryset().filter(
            savings_account__user=user,
            date__gte=first_day_of_queried_month,
            date__lte=last_day_of_the_queried_month
        )
        return spending_records
    

class Withdrawal(models.Model):
    custom_query = WithdrawalManager()
    objects = models.Manager()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(_("Date"), default=datetime.date.today)
    savings_account = models.ForeignKey(SavingsAccount, on_delete=models.CASCADE,
                                        null=True, blank=True)

    class Meta:
        ordering = ('savings_account', 'date')

    def __str__(self):
        return "{} | {} | Amount: {}".format(
            self.date,
            str(self.savings_account),
            self.amount,
        ).title()

