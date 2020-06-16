import random

from django.core.management.base import BaseCommand, CommandError

from motor_descuento.logica_negocio import ln_articulo
from motor_descuento.modelo.modelo_productos import Product


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        pass

    # pass parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        brand_id_list = [1, 2, 3, 4, 5]
        product_list = []
        is_create = False
        for numero in range(1, 100000):
            product = Product(name='Producto_' + str(numero), description='Producto_' + str(numero), tax_rate=12)
            product.brand_id = random.choice(brand_id_list)
            product_list.append(product)
        is_create = ln_articulo.crear_producto_list(product_list)
        # self.assertEqual(True, is_create)
