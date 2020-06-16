import decimal
import random

from django.core.management.base import BaseCommand, CommandError

from motor_descuento.logica_negocio import ln_articulo
from motor_descuento.modelo.modelo_productos import Product
from motor_descuento.modelo.modelo_retailer import StockItem


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        pass

    # pass parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        stock_ds = ln_articulo.consultar_product_id_list()
        categoria_ds = ln_articulo.consultar_categoria_id_list()
        producto_id_list = list(stock_ds)
        categoria_id_list = list(categoria_ds)
        retailer_id_list = [1, 2, 3, 4, 5]
        product_retailer_list = []
        for retailer in retailer_id_list:
            i = 0
            producto_id_list_temp = []
            while i < 10000:
                producto_id = random.choice(producto_id_list)
                product_search = list(filter(lambda x: x == producto_id, producto_id_list_temp))
                # print(i)
                if (len(product_search) == 0):
                    producto_id_list_temp.append(producto_id);
                    stock_item = StockItem(retailer_id=retailer, product_id=producto_id,
                                           categorie_id=random.choice(categoria_id_list), margin=2.0,
                                           pvp=float(decimal.Decimal(random.randrange(100, 999)) / 100))
                    product_retailer_list.append(stock_item)
                    i = i + 1
        ln_articulo.crear_retailer_product_list(product_retailer_list)
