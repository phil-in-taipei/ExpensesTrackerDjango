# Generated by Django 4.2.1 on 2023-06-12 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='incomesource',
            options={'ordering': ('income_source_name',)},
        ),
    ]
