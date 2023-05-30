from django.db import models


class Currency(models.Model):
    currency_code = models.CharField(max_length=3)
    currency_name = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "currencies"

    def __str__(self):
        return "{} ({})".format(
            self.currency_code,
            self.currency_name
        )
