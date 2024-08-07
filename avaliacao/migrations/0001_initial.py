# Generated by Django 5.0.2 on 2024-07-27 15:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('funcionario', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
                ('atendimento', models.IntegerField(choices=[(1, 'Muito Ruim'), (2, 'Ruim'), (3, 'Regular'), (4, 'Bom'), (5, 'Muito Bom')])),
                ('produto_servico', models.IntegerField(choices=[(1, 'Muito Ruim'), (2, 'Ruim'), (3, 'Regular'), (4, 'Bom'), (5, 'Muito Bom')])),
                ('comentarios', models.TextField(blank=True, null=True)),
                ('data', models.DateField(blank=True, default='2024-07-27')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funcionario.funcionario')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
