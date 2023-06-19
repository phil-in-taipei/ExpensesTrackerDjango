import datetime
from dateutil.relativedelta import relativedelta
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


class SpendingRecordManager(models.Manager):
    def users_spending_records_for_current_month(self, user):
        today = datetime.date.today()
        first_day_of_this_month = datetime.date(today.year, today.month, 1)
        first_day_of_next_month = first_day_of_this_month + relativedelta(months=1)
        last_day_of_this_month = first_day_of_next_month - relativedelta(days=1)
        spending_records = [
            spending_record for spending_record in self.get_queryset()
            if spending_record.expense.user == user and
            last_day_of_this_month >= spending_record.date >= first_day_of_this_month
        ]
        return spending_records

    def users_spending_records_for_queried_month_and_year(self, user, month, year):
        first_day_of_queried_month = datetime.date(year, month, 1)
        first_day_of_the_following_month = first_day_of_queried_month + relativedelta(months=1)
        last_day_of_the_queried_month = first_day_of_the_following_month - relativedelta(days=1)
        spending_records = [
            spending_record for spending_record in self.get_queryset()
            if spending_record.expense.user == user and
            last_day_of_the_queried_month >= spending_record.date >= first_day_of_queried_month
        ]
        return spending_records


class SpendingRecord(models.Model):
    custom_query = SpendingRecordManager()
    objects = models.Manager()
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
