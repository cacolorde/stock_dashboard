# Generated by Django 3.0.6 on 2020-06-01 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20200601_1623'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='wallet',
            unique_together={('owner', 'stock')},
        ),
    ]