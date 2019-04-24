# Generated by Django 2.0.6 on 2019-04-11 20:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userstory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoolModelBro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limited_integer_field', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.AlterField(
            model_name='userstory',
            name='prioridad',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='userstory',
            name='priorizacion',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='userstory',
            name='valor_negocio',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='userstory',
            name='valor_tecnico',
            field=models.PositiveIntegerField(),
        ),
    ]
