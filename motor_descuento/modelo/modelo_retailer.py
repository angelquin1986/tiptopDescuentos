from django.db import models

from motor_descuento.modelo.modelo_geolocalizacion import City, Sector
from motor_descuento.modelo.modelo_productos import Categorie
from motor_descuento.modelo.modelo_productos import Product

"""
@Author Aquingaluisa
Modelos de tipti para retailer
"""


class Retailer(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        db_table = 'retailer'


class RetailerCategories(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    class Meta:
        db_table = 'retailer_categories'


class RetailerCoverageSector(models.Model):
    enabled = models.BooleanField(default=True)
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)

    class Meta:
        db_table = 'retailer_coverage_sector'


class StockItem(models.Model):
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    pvp = models.DecimalField(max_digits=10, decimal_places=2)
    margin = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'stock_item'
        unique_together = (("retailer", "product"),)
