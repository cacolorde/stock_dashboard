# Generated by Django 3.0.5 on 2020-06-20 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20200616_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='is_etf',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='stock',
            name='is_fund',
            field=models.BooleanField(default=False),
        ),
    ]
