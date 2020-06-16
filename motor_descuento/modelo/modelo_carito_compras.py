from django.db import models

from motor_descuento.modelo.modelo_cliente import Client
from motor_descuento.modelo.modelo_retailer import StockItem

"""
@Author Aquingaluisa
Modelos de tipti para carito de compras
"""


class ShoopingCar(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'shooping_car'


class ShoopingCarItems(models.Model):
    shooping_car = models.ForeignKey(ShoopingCar, on_delete=models.CASCADE)
    stock_item = models.ForeignKey(StockItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    note_for_shopper = models.TextField()

    class Meta:
        db_table = 'shooping_car_items'


class ClientShoopingCar(models.Model):
    date_joined = models.DateField()
    menbers = models.IntegerField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        db_table = 'client_shooping_car'
