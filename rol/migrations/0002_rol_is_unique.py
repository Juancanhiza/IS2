# Generated by Django 2.0.6 on 2019-05-26 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rol', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rol',
            name='is_unique',
            field=models.BooleanField(default=False, verbose_name='Es único en el proyecto'),
        ),
    ]