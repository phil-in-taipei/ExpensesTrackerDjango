# Generated by Django 4.2.1 on 2023-06-27 04:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('income', '0003_alter_incomesource_options'),
        ('financial_accounts', '0004_remove_savingsaccount_currency_code_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Withdrawal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('savings_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='financial_accounts.savingsaccount')),
            ],
            options={
                'ordering': ('savings_account', 'date'),
            },
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('income_source', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='income.incomesource')),
                ('savings_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='financial_accounts.savingsaccount')),
            ],
            options={
                'ordering': ('savings_account', 'date'),
            },
        ),
    ]
