from django.conf import settings
from django.db import models


class IncomeSource(models.Model):
    income_source_name = models.CharField(max_length=250)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return "{}: {}".format(
            self.user,
            self.income_source_name
        ).title()


