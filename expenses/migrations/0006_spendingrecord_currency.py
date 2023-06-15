# Generated by Django 4.2.1 on 2023-06-14 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0002_alter_currency_options'),
        ('expenses', '0005_remove_spendingrecord_time_stamp_spendingrecord_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='spendingrecord',
            name='currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='currencies.currency'),
        ),
    ]