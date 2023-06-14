# Generated by Django 4.2.1 on 2023-06-14 11:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0004_alter_spendingrecord_time_stamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spendingrecord',
            name='time_stamp',
        ),
        migrations.AddField(
            model_name='spendingrecord',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
