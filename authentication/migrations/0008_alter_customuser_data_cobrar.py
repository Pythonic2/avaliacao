# Generated by Django 5.0.2 on 2024-06-27 01:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_alter_customuser_data_cobrar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='data_cobrar',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 27, 1, 59, 0, 282049, tzinfo=datetime.timezone.utc)),
        ),
    ]