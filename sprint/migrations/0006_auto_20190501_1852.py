# Generated by Django 2.0.6 on 2019-05-01 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '0005_auto_20190429_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprint',
            name='estado',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('En Proceso', 'En Proceso'), ('Terminado', 'Terminado')], default='Pendiente', max_length=25),
        ),
    ]
