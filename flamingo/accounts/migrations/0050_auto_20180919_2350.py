# Generated by Django 2.1 on 2018-09-19 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0049_auto_20180919_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='available',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='accounts.Available', verbose_name='Car Available'),
        ),
    ]
