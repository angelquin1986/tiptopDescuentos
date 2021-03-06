# Generated by Django 3.0.7 on 2020-06-16 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motor_descuento', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disccount',
            name='email',
        ),
        migrations.RemoveField(
            model_name='disccount',
            name='last_name',
        ),
        migrations.AddField(
            model_name='primesuscription',
            name='vality',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='clientprimesuscription',
            name='activation_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='clientshoopingcar',
            name='date_joined',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='clientshoopingcar',
            name='menbers',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='disccount',
            name='fecha_fin',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='disccount',
            name='fecha_inicio',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='disccount',
            name='hora_fin',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='disccount',
            name='hora_inicio',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='disccount',
            name='monto_actual',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='disccount',
            name='monto_maximo',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='primesuscription',
            name='vality_type',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='shoopingcaritems',
            name='note_for_shopper',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='shoopingcaritems',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]
