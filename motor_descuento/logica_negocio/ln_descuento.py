"""
@authos descuento logica de negocio
"""
import copy
from datetime import datetime

from motor_descuento.modelo.modelo_cliente import ClientPrimeSuscription
from motor_descuento.modelo.modelo_descuentos import Disccount
from motor_descuento.modelo.modelo_productos import Product
from motor_descuento.modelo.modelo_retailer import StockItem


def obtener_descuento_list():
    """
    retorna lista de  descuentos de base
    :return:
    """
    return Disccount.objects.all()


def motor_descuento(fecha_actual, stock_item_list_parameter, client_id, codigo_forma_pago,
                    codigo_aplicacion_parametro):
    """
    metodo principal para resilver los descuentos mediante el motor construido
    :param fecha_actual:
    :param stock_item_list_parameter:
    :param client_id:
    :param codigo_forma_pago:
    :param codigo_aplicacion_parametro:
    :return:
    """
    # colocamos los datos principales a  los articulos
    stock_item_list = copy.deepcopy(stock_item_list_parameter)
    product_id_list = [stock_item['product_id'] for stock_item in stock_item_list]
    retailer_id_list = [stock_item['retailer_id'] for stock_item in stock_item_list]
    product_db_list = Product.objects.filter(id__in=product_id_list,
                                             stockitem__retailer_id__in=retailer_id_list).values('id',
                                                                                                 'brand_id',
                                                                                                 'stockitem__pvp',
                                                                                                 'stockitem__retailer_id',
                                                                                                 'stockitem__categorie_id',
                                                                                                 'stockitem__categorie__subcategorie__id')
    # .prefetch_related('stockitem_set__categorie__subcategorie_set', 'stockitem_set__retailer')

    # consultamos la configuiracion de descuento por fechas
    discount_list = list(Disccount.objects.filter(fecha_inicio__lte=fecha_actual, fecha_fin__gte=fecha_actual).order_by(
        'prioridad').values())
    product_descuento_list = []
    for descuento in discount_list:
        json_data = descuento['json_data']
        cliente_prime = validar_cliente_prime(client_id, json_data['es_cliente_prime'])
        activa_promocion_dia = validar_dia_semana_promocion(fecha_actual, json_data['dia_promocion'])
        activa_promocion_hora = validar_hora_aplicacion(descuento['hora_inicio'], descuento['hora_fin'])
        activa_codigo_aplicacion = validar_codigo_aplicacion_descuento(codigo_aplicacion_parametro,
                                                                       json_data['codigo_aplicacion'])
        activa_forma_pago_descuento = validar_forma_pago_descuento(codigo_forma_pago, json_data['forma_pago'])
        # validaciones de cliente primer y dia por promocion de una fecha especifica
        if stock_item_list and cliente_prime and activa_promocion_dia and activa_promocion_hora and activa_codigo_aplicacion and activa_forma_pago_descuento:

            # cliente
            if json_data['product_id'] != None and len(json_data['product_id']) > 0:
                product_list = descuento_por_producto(json_data['product_id'], json_data['retailer_id'],
                                                      stock_item_list,
                                                      product_db_list, descuento['descuento'])
                product_descuento_list.extend(product_list)
                # categoria
            if json_data['category_id'] != None and len(json_data['category_id']) > 0:
                product_list = descuento_por_categoria(json_data['category_id'], json_data['retailer_id'],
                                                       stock_item_list,
                                                       product_db_list, descuento['descuento'])
                product_descuento_list.extend(product_list)
                # subcategoria
            if json_data['sub_category_id'] is not None and len(
                    json_data['sub_category_id']) > 0 and cliente_prime:
                product_list = descuento_por_cliente(json_data['sub_category_id'], json_data['retailer_id'],
                                                     stock_item_list,
                                                     product_db_list, descuento['descuento'])
                product_descuento_list.extend(product_list)
                # cliente
            if json_data['client_id'] != None and len(json_data['client_id']) > 0:
                product_list = descuento_por_cliente(json_data['client_id'], stock_item_list,
                                                     product_db_list, descuento['descuento'], client_id)
                product_descuento_list.extend(product_list)
                # marca
            if json_data['brand_id'] != None and len(json_data['brand_id']) > 0:
                product_list = descuento_por_marca(json_data['brand_id'], stock_item_list,
                                                   product_db_list, descuento['descuento'])
                product_descuento_list.extend(product_list)

    # tomamos los descuentos por  fecha actual
    result = construir_objeto_final_descuento(product_descuento_list, stock_item_list_parameter)
    print("resultado", result)
    return result


def resolver_descuento(fecha_actual, stock_item_list_parameter, client_id, codigo_forma_pago,
                       codigo_aplicacion_parametro):
    """
    Resuelve el descuento   de una lista de stock parametro enviada
    :param fecha_inicio:
    :param fecha_fin:
    :return:
    """

    return motor_descuento(fecha_actual, stock_item_list_parameter, client_id, codigo_forma_pago,
                           codigo_aplicacion_parametro)


def resolver_descuento_tienda(fecha_actual, retailer_id):
    """
    Resuelve el descuento   de una una tienda especifica enviada como parametro
    :param fecha_inicio:
    :param fecha_fin:
    :return:
    """
    stock_item_list = list(StockItem.objects.filter(retailer_id=retailer_id).values('retailer_id', 'product_id'))
    return motor_descuento(fecha_actual, stock_item_list, None, None, None)


def construir_objeto_final_descuento(product_descuento_list, stock_item_list_parameter):
    """
    Contruir un objeto general con los articulos que aplica y no aplica descuentos
    :param product_descuento_list:
    :param stock_item_list_parameter:
    :return:
    """
    list_descuentos = []
    for stock_item in stock_item_list_parameter:
        descuento_obj = {}
        product_descuento = next(filter(
            lambda x: x['id'] == stock_item['product_id'] and x['stockitem__retailer_id'] == stock_item['retailer_id'],
            product_descuento_list), None)
        if (product_descuento):
            descuento_obj = {
                'product_id': product_descuento['id'],
                'retailer_id': product_descuento['stockitem__retailer_id'],
                'pvp': product_descuento['stockitem__pvp'],
                'descuento': product_descuento['descuento'],
                'descuento_porcentaje': product_descuento['descuento_porcentaje'],
                'tipo_descuento': product_descuento['tipo_descuento'],
            }
            list_descuentos.append(descuento_obj)
        else:
            descuento_obj = {
                'product_id': stock_item['product_id'],
                'retailer_id': stock_item['retailer_id'],
                'pvp': 0.0,
                'descuento': 0.0,
                'descuento_porcentaje': 0.0,
                'tipo_descuento': 'n/a',
            }
            list_descuentos.append(descuento_obj)
    return list_descuentos


def validar_forma_pago_descuento(codigo_forma_pago, descuento_forma_pago):
    """
    validar forma de pago para una conf descuento
    :param codigo_forma_pago:
    :param descuento_forma_pago:
    :return:
    """
    if codigo_forma_pago and descuento_forma_pago:
        if codigo_forma_pago == descuento_forma_pago:
            return True
        else:
            return False
    else:
        return True


def validar_codigo_aplicacion_descuento(codigo_aplicacion, descuento_codigo_aplicacion):
    """
    validar que exista con digo de aplicacion
    :param codigo_aplicacion:
    :param descuento_dia_promocion:
    :return:
    """
    if codigo_aplicacion and descuento_codigo_aplicacion:
        if codigo_aplicacion == descuento_codigo_aplicacion:
            return True
        else:
            return False
    else:
        return True


def validar_hora_aplicacion(hora_inicio, hora_fin):
    """
    validar si se puede usar   la conf descuentos por hora inicio o fin
    :param hora_inicio:
    :param hora_fin:
    :return:
    """
    if hora_inicio and hora_inicio:
        hora_actual = datetime.now().time()
        # h_inicio = datetime.strptime(hora_inicio, '%H::%M::%S').time()
        # h_fin = datetime.strptime(hora_fin, '%H::%M::%S').time()
        # validar si esta dentro del rango de horas
        if hora_actual >= hora_inicio and hora_actual <= hora_fin:
            return True
        else:
            return False
    else:
        return True


def validar_dia_semana_promocion(fecha_actual, descuento_dia_promocion_list):
    """
    Valida si se aplica un descuento por dia  segun el parametro
    :param fecha_actual:
    :param descuento_dia_promocion_list:
    :return:
    """
    # tomar la fecha en date
    fecha_actual_date = datetime.strptime(fecha_actual, '%Y-%m-%d').date()
    # tomar el dia de la semana en formato integer
    dia_fechaParametro = fecha_actual_date.weekday()
    # validar si  el dia de la promcion esta activo
    if descuento_dia_promocion_list:
        dias_list = list(filter(lambda x: x == dia_fechaParametro, descuento_dia_promocion_list))
        if len(dias_list) > 0:
            return True
        else:
            return False
    else:
        return True


def validar_cliente_prime(cliente_id_parameter, descuento_es_cliente_prime):
    """
    validar si es un cliente prime para aplicar los desccuentos respectivos
    :param cliente_id_parameter:
    :param descuento_es_cliente_prime:
    :return:
    """
    # solo si el descuento es para clientes prime
    if (cliente_id_parameter and descuento_es_cliente_prime):
        # buscar el cliente en base y validar si tiene bandera prime
        client_prime__subcripcion = ClientPrimeSuscription.objects.filter(client_id=cliente_id_parameter,
                                                                          suscription_state=True).values_list('id',
                                                                                                              flat=True)
        if (client_prime__subcripcion):
            return True
        else:
            return False
    return True


def calcular_descuento(porcentaje, pvp):
    """
    Metodo para calculo sw un descuento
    :param porcentaje:
    :param pvp:
    :return:
    """

    return (pvp * porcentaje) / 100


def descuento_por_producto(descuento_product_id_list, descuento_retailer_id_list, stock_item_list, product_db_list,
                           descuento):
    """
    Calcula  el descuento cuanto la parametrizacion es por producto
    :param descuento_product_id_list:
    :param descuento_retailer_id_list:
    :param stock_item_list:
    :param product_db_list:
    :param descuento:
    :return:
    """
    stock_item_list_search = None;
    list_product_discount = []
    # caso de todos los productos  sin tienda
    if (descuento_retailer_id_list == None or len(descuento_retailer_id_list) == 0):
        # buscar los productos de la conf de descuentos en stock_item parametro solo por articulo
        stock_item_list_search = list(filter(lambda x: x['product_id'] in descuento_product_id_list, stock_item_list))
    else:
        # buscar los productos de la conf de descuentos en stock_item parametro solo por articulo/retailer
        stock_item_list_search = list(filter(
            lambda x: x['product_id'] in descuento_product_id_list and x['retailer_id'] in descuento_retailer_id_list,
            stock_item_list))
        # buscar los productos en la los datos de la base para tomar el pvp
    if (stock_item_list_search):
        for p in stock_item_list_search:
            producto = next(
                filter(lambda x: x['id'] == p['product_id'] and x['stockitem__retailer_id'] == p['retailer_id'],
                       product_db_list), None)
            producto['descuento'] = calcular_descuento(descuento, producto['stockitem__pvp'])
            producto['descuento_porcentaje'] = descuento
            producto['tipo_descuento'] = 'art'
            list_product_discount.append(producto)
            # eliminar el stock utilizado  en el descuento de la colecion original
            stock_item_list.remove(p)
    return list_product_discount


def descuento_por_categoria(descuento_categoria_id_list, descuento_retailer_id_list, stock_item_list, product_db_list,
                            descuento):
    """
    Calcula  el descuento cuanto la parametrizacion es por categoria
    :param descuento_product_id_list:
    :param descuento_retailer_id_list:
    :param stock_item_list:
    :param product_db_list:
    :param descuento:
    :return:
    """
    product_search = None;
    list_product_discount = []
    product_list_general = []
    # iteramos el stock_items para tomar los datos de base
    for stock in stock_item_list:
        product_list = list(
            filter(lambda x: stock['product_id'] == x['id'] and stock['retailer_id'] == x['stockitem__retailer_id'],
                   product_db_list))
        product_list_general.extend(product_list)
    # cuando no  tiene tienda especifica
    if (descuento_retailer_id_list == None or len(descuento_retailer_id_list) == 0):
        product_search = list(filter(lambda x: stock['product_id'] == x['id'] and x[
            'stockitem__categorie_id'] in descuento_categoria_id_list,
                                     product_list_general))
    else:
        # buscar los productos de la conf de descuentos en stock_item parametro solo por categoria/retailer
        product_search = list(filter(
            lambda x: stock['product_id'] == x['id'] and x['stockitem__retailer_id'] in descuento_retailer_id_list and
                      x[
                          'stockitem__categorie_id'] in descuento_categoria_id_list,
            product_list_general))
        # buscar los productos en la los datos de la base para tomar el pvp
    if (product_search):
        for p in product_search:
            stock_item = next(
                filter(lambda x: x['product_id'] == p['id'] and x['retailer_id'] == p['stockitem__retailer_id'],
                       stock_item_list), None)
            if (stock_item):
                p['descuento'] = calcular_descuento(descuento, p['stockitem__pvp'])
                p['descuento_porcentaje'] = descuento
                p['tipo_descuento'] = 'cat'
                list_product_discount.append(p)
                stock_item_list.remove(stock_item)
    return list_product_discount


def descuento_por_sub_categoria(descuento_sub_categoria_id_list, descuento_retailer_id_list, stock_item_list,
                                product_db_list,
                                descuento):
    """
    Calcula  el descuento cuanto la parametrizacion es por sub categoria
    :param descuento_product_id_list:
    :param descuento_retailer_id_list:
    :param stock_item_list:
    :param product_db_list:
    :param descuento:
    :return:
    """
    product_search = None;
    list_product_discount = []
    product_list_general = []
    # iteramos el stock_items para tomar los datos de base
    for stock in stock_item_list:
        product_list = list(
            filter(lambda x: stock['product_id'] == x['id'] and stock['retailer_id'] == x['stockitem__retailer_id'],
                   product_db_list))
        product_list_general.extend(product_list)
    # cuando no  tiene tienda especifica
    if (descuento_retailer_id_list == None or len(descuento_retailer_id_list) == 0):
        product_search = list(filter(lambda x: stock['product_id'] == x['id'] and x[
            'stockitem__categorie__subcategorie__id'] in descuento_sub_categoria_id_list,
                                     product_list_general))
    else:
        # buscar los productos de la conf de descuentos en stock_item parametro solo por categoria/retailer
        product_search = list(filter(
            lambda x: stock['product_id'] == x['id'] and x['stockitem__retailer_id'] in descuento_retailer_id_list and
                      x['stockitem__categorie__subcategorie__id'] in descuento_sub_categoria_id_list,
            product_list_general))
        # buscar los productos en la los datos de la base para tomar el pvp
    if (product_search):
        for p in product_search:
            stock_item = next(
                filter(lambda x: x['product_id'] == p['id'] and x['retailer_id'] == p['stockitem__retailer_id'],
                       stock_item_list), None)
            if (stock_item):
                p['descuento'] = calcular_descuento(descuento, p['stockitem__pvp'])
                p['descuento_porcentaje'] = descuento
                p['tipo_descuento'] = 'sct'
                list_product_discount.append(p)
                stock_item_list.remove(stock_item)
    return list_product_discount


def descuento_por_cliente(descuento_cliente_id_list, stock_item_list,
                          product_db_list,
                          descuento, client_id):
    """
    Descuento por cliente , valida si el cliente se encuentra el la configuracion de  descuento
    :param descuento_cliente_id_list:
    :param stock_item_list:
    :param product_db_list:
    :param descuento:
    :param client_id:
    :return:
    """
    # buscamos el cliente en el parametro de descuento
    descuento_client_id = next(filter(lambda x: x == client_id, descuento_cliente_id_list), None)
    list_product_discount = []
    if (descuento_client_id):
        product_list_general = []
        # iteramos el stock_items para tomar los datos de base
        for stock in stock_item_list:
            product_list = list(
                filter(lambda x: stock['product_id'] == x['id'] and stock['retailer_id'] == x['stockitem__retailer_id'],
                       product_db_list))
            product_list_general.extend(product_list)
        if (product_list_general):
            for p in product_list_general:
                stock_item = next(
                    filter(lambda x: x['product_id'] == p['id'] and x['retailer_id'] == p['stockitem__retailer_id'],
                           stock_item_list), None)
                if (stock_item):
                    p['descuento'] = calcular_descuento(descuento, p['stockitem__pvp'])
                    p['descuento_porcentaje'] = descuento
                    p['tipo_descuento'] = 'cli'
                    list_product_discount.append(p)
                    stock_item_list.remove(stock_item)
    return list_product_discount


def descuento_por_marca(descuento_marca_id_list, stock_item_list, product_db_list, descuento):
    """
    Descuento por cliente , valida si el cliente se encuentra el la configuracion de  descuento
    :param descuento_cliente_id_list:
    :param stock_item_list:
    :param product_db_list:
    :param descuento:
    :param client_id:
    :return:
    """
    list_product_discount = []
    product_list_general = []
    # buscamos los articulos con la marca del descuento
    producto_x_marca_list = list(filter(lambda x: x['brand_id'] in descuento_marca_id_list, product_db_list))
    for stock in stock_item_list:
        product_list = list(
            filter(lambda x: stock['product_id'] == x['id'] and stock['retailer_id'] == x['stockitem__retailer_id'],
                   producto_x_marca_list))
        product_list_general.extend(product_list)
    if (product_list_general):
        for p in product_list_general:
            stock_item = next(
                filter(lambda x: x['product_id'] == p['id'] and x['retailer_id'] == p['stockitem__retailer_id'],
                       stock_item_list), None)
            if (stock_item):
                p['descuento'] = calcular_descuento(descuento, p['stockitem__pvp'])
                p['descuento_porcentaje'] = descuento
                p['tipo_descuento'] = 'mar'
                list_product_discount.append(p)
                stock_item_list.remove(stock_item)
    return list_product_discount
