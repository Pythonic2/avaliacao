# Generated by Django 5.0.2 on 2024-02-14 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='qrcode',
            field=models.ImageField(blank=True, upload_to='code'),
        ),
    ]
