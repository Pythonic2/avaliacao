# Generated by Django 5.0.2 on 2024-07-01 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao', '0002_alter_avaliacao_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='data',
            field=models.DateField(blank=True, default='2024-07-01'),
        ),
    ]
