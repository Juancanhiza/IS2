# Generated by Django 2.0.6 on 2019-04-26 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0001_initial'),
        ('userstory', '0005_userstory_team_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='proyecto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='proyecto.Proyecto'),
        ),
    ]
