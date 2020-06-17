"""
@author aquingaluisa
"""
# Cargamos el módulo unittest

import pytest
from django.test import TestCase, override_settings

from motor_descuento.logica_negocio import ln_descuento
# Creamos una clase heredando de TestCase
from motor_descuento.test import util_test
from motor_descuento.test.util_test import show_sql


class TestDescuentos(TestCase):
    fixtures = ['db.json', 'descuento.json']
    stock_item = [{'product_id': 1, 'retailer_id': 1}, {'product_id': 2, 'retailer_id': 1},
                  {'product_id': 3, 'retailer_id': 1}]
    cliente_id = 1

    def setUp(self):
        util_test.product()
        util_test.stok_items()

    @pytest.mark.django_db
    @override_settings(DEBUG=True)
    def test_descuento_x_articulo(self):
        """
        Probar los descuento por articulos mediante la parametrizacion
        :return:
        """
        show_sql()

        # producto
        ln_descuento.resolver_descuento('2020-06-16', self.stock_item, self.cliente_id)

    @pytest.mark.django_db
    @override_settings(DEBUG=True)
    def test_descueto_x_categoria(self):
        """
        Probar los descuentos por  categoria mediante parametrizacion
        :return:
        """
        # categoria
        ln_descuento.resolver_descuento('2020-01-20', self.stock_item, self.cliente_id)

    @pytest.mark.django_db
    @override_settings(DEBUG=True)
    def test_descueto_x_sub_categoria(self):
        """
        Probar los descuentos por  categoria mediante parametrizacion
        :return:
        """

        # subcategoria
        ln_descuento.resolver_descuento('2019-01-20', self.stock_item, self.cliente_id)

    @pytest.mark.django_db
    @override_settings(DEBUG=True)
    def test_descueto_x_cliente(self):
        """
        Probar los descuentos por  cliente mediante parametrizacion
        :return:
        """

        # subcategoria
        ln_descuento.resolver_descuento('2019-02-15', self.stock_item, self.cliente_id)

    @pytest.mark.django_db
    @override_settings(DEBUG=True)
    def test_descueto_x_cliente_prime(self):
        """
        Probar los descuentos por  cliente mediante parametrizacion
        :return:
        """
        cliente_id_no_prime = 3
        # subcategoria
        ln_descuento.resolver_descuento('2019-02-15', self.stock_item, cliente_id_no_prime)

    @pytest.mark.django_db
    @override_settings(DEBUG=True)
    def test_descueto_x_marca(self):
        """
        Probar los descuentos por  cliente mediante parametrizacion
        :return:
        """
        cliente_id_no_prime = 1
        # subcategoria
        ln_descuento.resolver_descuento('2019-03-11', self.stock_item, cliente_id_no_prime)
