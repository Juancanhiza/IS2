# Generated by Django 2.0.6 on 2019-05-26 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0004_auto_20190526_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]
