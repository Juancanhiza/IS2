# Generated by Django 2.0.6 on 2019-04-25 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proyecto', '0001_initial'),
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
                ('proyecto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='proyecto.Proyecto')),
            ],
        ),
    ]
