# Generated by Django 2.0.6 on 2019-03-29 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_auto_20190329_0243'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_usuario', models.CharField(max_length=100)),
                ('apellido_usuario', models.CharField(max_length=100)),
                ('contraseña_usuario', models.CharField(max_length=100)),
                ('estado_usuario', models.CharField(max_length=100)),
                ('ci_usuario', models.CharField(max_length=10)),
                ('telefono_usuario', models.CharField(max_length=50)),
                ('direccion_usuario', models.CharField(max_length=200)),
                ('descripcion_usuario', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='agregarusuario',
            name='user',
        ),
        migrations.DeleteModel(
            name='AgregarUsuario',
        ),
    ]
