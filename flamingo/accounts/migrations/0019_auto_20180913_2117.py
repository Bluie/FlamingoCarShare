# Generated by Django 2.1 on 2018-09-13 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20180913_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='image',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='accounts.Car'),
        ),
    ]
