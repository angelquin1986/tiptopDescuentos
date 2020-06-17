from django.contrib.postgres.fields import JSONField
from django.db import models

"""
@Author Aquingaluisa
Modelos de tipti para retailer
"""


class Disccount(models.Model):
    json_data = JSONField()
    descuento = models.IntegerField(null=True)
    monto_maximo = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    monto_actual = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    # last_name = models.CharField(max_length=50)
    fecha_inicio = models.DateField(null=True)
    fecha_fin = models.DateField(null=True)
    hora_inicio = models.TimeField(null=True)
    hora_fin = models.TimeField(null=True)
    prioridad = models.IntegerField(null=True)

    # email = models.CharField(max_length=50)

    class Meta:
        db_table = 'disccount'
