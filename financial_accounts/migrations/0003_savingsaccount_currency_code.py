# Generated by Django 4.2.1 on 2023-05-29 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_accounts', '0002_savingsaccount_account_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='savingsaccount',
            name='currency_code',
            field=models.CharField(choices=[('TWD', 'Taiwan New Dollar'), ('USD', 'United States Dollar'), ('EUR', 'Euro Member Countries')], default='TWD', max_length=200),
        ),
    ]
