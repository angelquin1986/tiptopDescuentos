from django.db import models

"""
@Author Aquingaluisa
Modelos de tipti para clientes
"""


class Client(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    class Meta:
        db_table = 'client'


class PrimeSuscription(models.Model):
    name = models.CharField(max_length=50)
    vality = models.IntegerField
    vality_type = models.CharField(max_length=50)
    enabled = models.BooleanField(default=True)

    class Meta:
        db_table = 'prime_suscription'


class ClientPrimeSuscription(models.Model):
    prime_suscription = models.ForeignKey(PrimeSuscription, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    activation_date = models.DateField()
    suscription_state = models.BooleanField(default=True)

    class Meta:
        db_table = 'client_prime_suscription'
