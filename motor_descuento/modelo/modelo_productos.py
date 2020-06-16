from django.db import models

"""
@Author Aquingaluisa
Modelos de tipti para productos
"""


class Brand(models.Model):
    """
    Modelo para marcas
    """
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'brand'


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    tax_rate = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    # brand_id = models.IntegerField(db_column='brand_id')

    class Meta:
        db_table = 'product'


class Categorie(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        db_table = 'categorie'


class Subcategorie(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    class Meta:
        db_table = 'subcategorie'
