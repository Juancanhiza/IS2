# Generated by Django 2.0.6 on 2019-04-22 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('fecha_inicio', models.DateField(verbose_name='Fecha de Inicio Sprint')),
                ('fecha_fin', models.DateField(verbose_name='Fecha de Fin Sprint')),
                ('duracion', models.DurationField()),
            ],
        ),
    ]
