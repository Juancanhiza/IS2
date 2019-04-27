# Generated by Django 2.0.6 on 2019-04-26 22:10

from django.db import migrations, models
import django.db.models.deletion
import userstory.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proyecto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserStory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=300)),
                ('fecha_inicio', models.DateField(verbose_name='Fecha de inicio del User Story')),
                ('duracion_estimada', models.DurationField()),
                ('valor_negocio', models.PositiveIntegerField(validators=[userstory.models.rango])),
                ('prioridad', models.PositiveIntegerField(validators=[userstory.models.rango])),
                ('valor_tecnico', models.PositiveIntegerField(validators=[userstory.models.rango])),
                ('estado', models.PositiveIntegerField(choices=[(2, 'Pendiente'), (1, 'Asignado'), (0, 'Finalizado')], default=2)),
                ('proyecto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='proyecto.Proyecto')),
            ],
        ),
    ]