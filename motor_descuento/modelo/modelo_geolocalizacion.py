from django.db import models

"""
@Author Aquingaluisa
Modelos de tipti para localizacion geografica
"""


class Country(models.Model):
    name = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)
    lenguaje = models.CharField(max_length=50)
    currency = models.CharField(max_length=50)

    class Meta:
        db_table = 'country'


class Province(models.Model):
    name = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        db_table = 'province'


class City(models.Model):
    name = models.CharField(max_length=50)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    class Meta:
        db_table = 'city'


class Sector(models.Model):
    name = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        db_table = 'sector'


class Adrerss(models.Model):
    name = models.CharField(max_length=50)
    line_one = models.CharField(max_length=50)
    line_two = models.CharField(max_length=50)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)

    class Meta:
        db_table = 'adrerss'
