# Generated by Django 5.0.2 on 2024-06-27 02:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_alter_customuser_data_cobrar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='data_cobrar',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 27, 2, 5, 3, 573997, tzinfo=datetime.timezone.utc)),
        ),
    ]