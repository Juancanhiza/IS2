# Generated by Django 2.0.6 on 2019-03-29 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0009_auto_20190329_0639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='estado_usuario',
            field=models.CharField(choices=[('act', 'Activo'), ('ina', 'Inactivo')], default='act', max_length=3),
        ),
    ]
