# Generated by Django 4.2.1 on 2023-06-14 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0002_alter_incomesource_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='incomesource',
            options={'ordering': ('user', 'income_source_name')},
        ),
    ]