"""
@author aquingaluisa
Loginca de negocio para  articulos
"""
from django.db import transaction

from motor_descuento.modelo.modelo_productos import Product,Categorie
from motor_descuento.modelo.modelo_retailer import StockItem


@transaction.atomic
def crear_producto_list(product_list):
    """
    Crear productos de forma masiva
    """
    try:
        Product.objects.bulk_create(product_list)
        return True
    except Exception as e:
        print("no insert prodcuto", str(e))
        return False


def crear_retailer_product_list(stock_item_list):
    """
    crea la lista de  retailer con los artuculos
    :return:
    """
    try:
        StockItem.objects.bulk_create(stock_item_list)
    except Exception as e:
        print("no insert retailer_product_list", str(e))
    return False


def consultar_product_id_list():
    return Product.objects.values_list('id', flat=True)

def consultar_categoria_id_list():
    return Categorie.objects.values_list('id', flat=True)
