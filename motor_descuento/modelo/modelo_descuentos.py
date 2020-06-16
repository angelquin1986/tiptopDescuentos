from django.db import models

"""
@Author Aquingaluisa
Modelos de tipti para retailer
"""


class Disccount(models.Model):
    json_data = models.TextField()
    monto_maximo = models.DecimalField(max_digits=10, decimal_places=2)
    monto_actual = models.DecimalField(max_digits=10, decimal_places=2)
    last_name = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    email = models.CharField(max_length=50)

    class Meta:
        db_table = 'disccount'
