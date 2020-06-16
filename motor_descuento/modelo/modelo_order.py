from django.db import models

from motor_descuento.modelo.modelo_cliente import Client
from motor_descuento.modelo.modelo_retailer import Retailer, StockItem
from motor_descuento.modelo.modelo_geolocalizacion import Adrerss

"""
@Author Aquingaluisa
Modelos de tipti para orders
"""


class ClientOrder(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    adrerss = models.ForeignKey(Adrerss, on_delete=models.CASCADE)
    delivery_date = models.DateField()
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'client_order'


class OrderItem(models.Model):
    client_order = models.ForeignKey(ClientOrder, on_delete=models.CASCADE)
    stock_item = models.ForeignKey(StockItem, on_delete=models.CASCADE)
    pvp = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    note_for_shopper = models.TextField()
    pvp_with_discount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'order_item'
