from django.conf import settings
from django.db import models


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
