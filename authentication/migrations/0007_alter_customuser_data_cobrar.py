# Generated by Django 5.0.2 on 2024-08-21 22:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_alter_customuser_data_cobrar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='data_cobrar',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 20, 22, 52, 27, 313387, tzinfo=datetime.timezone.utc)),
        ),
    ]
