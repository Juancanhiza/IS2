# Generated by Django 2.0.6 on 2019-06-23 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userstory', '0014_auto_20190613_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='duracion_restante',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='userstory',
            name='duracion_estimada',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
