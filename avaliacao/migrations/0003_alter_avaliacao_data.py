# Generated by Django 5.0.2 on 2024-08-21 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao', '0002_alter_avaliacao_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='data',
            field=models.DateField(blank=True, default='2024-08-21'),
        ),
    ]
