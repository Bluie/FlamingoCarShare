# Generated by Django 2.1 on 2018-09-13 08:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20180913_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='book_end_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 13, 18, 57, 23, 368767)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='book_start_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 13, 18, 57, 23, 368767)),
        ),
    ]
