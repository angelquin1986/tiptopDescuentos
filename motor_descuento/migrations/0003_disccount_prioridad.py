# Generated by Django 3.0.7 on 2020-06-16 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motor_descuento', '0002_auto_20200616_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='disccount',
            name='prioridad',
            field=models.IntegerField(null=True),
        ),
    ]
