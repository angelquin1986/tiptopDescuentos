# scripts/carga_articulos.py
import random

from motor_descuento.logica_negocio import ln_articulo
from motor_descuento.modelo.modelo_productos import Product
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "descuentos.settings")

def run(self):
    brand_id_list = [1, 2, 3, 4, 5]
    product_list = []
    is_create = False
    for numero in [10000]:
        product = Product(name='Producto_' + str(numero), description='Producto_' + str(numero), tax_rate=12)
        product.brand_id = random.choice(brand_id_list)
        product_list.append(product)
        is_create = ln_articulo.crear_producto_list(product_list)
    self.assertEqual(True, is_create)
