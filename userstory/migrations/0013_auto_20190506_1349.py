# Generated by Django 2.0.6 on 2019-05-06 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userstory', '0012_auto_20190506_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstory',
            name='sprint_asignados',
            field=models.ManyToManyField(blank=True, null=True, related_name='userstory_sprint_asignado', to='sprint.Sprint'),
        ),
    ]