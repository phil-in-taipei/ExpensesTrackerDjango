# Generated by Django 4.2.1 on 2023-06-12 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currency',
            options={'verbose_name_plural': 'currencies'},
        ),
    ]
