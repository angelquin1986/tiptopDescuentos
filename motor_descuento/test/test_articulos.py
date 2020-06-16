"""
@author aquingaluisa
"""
# Cargamos el módulo unittest
import os
import random

import pytest
from django.test import TestCase

# Creamos una clase heredando de TestCase
from motor_descuento.logica_negocio import ln_articulo as ln_articulo
from motor_descuento.modelo.modelo_productos import Product
from motor_descuento.test import util_test


class TestArticulos(TestCase):
    fixtures = ['db.json']

    def setUp(self):
        util_test.product();
        util_test.stok_items()

    # Creamos una prueba para probar un valor inicial
    @pytest.mark.django_db
    def test_crear_articulos(self):
        categorias_list = list(ln_articulo.consultar_categoria_id_list())
        producto_list = list(ln_articulo.consultar_product_id_list())
        stok_list = list(ln_articulo.consultar_stock_id_list())

        print(categorias_list)
        print(producto_list)
        print(stok_list)
        brand_id_list = [1, 2, 3, 4, 5]
        # product_list = []
        # is_create = False
        # for numero in [10000]:
        #     product = Product(name='Producto_' + str(numero), description='Producto_' + str(numero), tax_rate=12)
        #     product.brand_id = random.choice(brand_id_list)
        #     product_list.append(product)
        #     is_create = ln_articulo.crear_producto_list(product_list)
        # self.assertEqual(True, is_create)
