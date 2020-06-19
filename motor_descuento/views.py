from django.forms import model_to_dict
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from motor_descuento.modelo.modelo_descuentos import Disccount
from motor_descuento.modelo.modelo_retailer import Retailer
from .serializers import DisccountSerializer
from motor_descuento.logica_negocio import ln_descuento

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


class DisccountViewSet(viewsets.ModelViewSet):
    queryset = Disccount.objects.all().order_by('name')
    serializer_class = DisccountSerializer


@api_view(['GET', ])
def descuentos_list(request):
    """
    List de conf desceuntos
    """
    if request.method == 'GET':
        descuentos_list = list(Disccount.objects.all())
        serialized_obj = [model_to_dict(descuento) for descuento in descuentos_list]
        return Response(serialized_obj)


@api_view(['GET', ])
def retailer_list(request):
    """
    Lista de tiendas
    """
    if request.method == 'GET':
        retailer_list = list(Retailer.objects.all())
        serialized_obj = [model_to_dict(retailer) for retailer in retailer_list]
        # json.loads(serialized_obj)
        # serialized_obj = serializers.serialize('json', retailer_list)
        # serializer = SnippetSerializer(snippets, many=True)
        return Response(serialized_obj)


@api_view(['POST'])
def obtener_descuento(request):
    """

    :return:
    """
    data = request.data

    resultado = ln_descuento.resolver_descuento(data['fecha_actual'], data['stock_item'], data['cliente_id'],
                                                data['codigo_forma_pago'], data['codigo_aplicacion'])
    print("")
    return Response(resultado)


@api_view(['POST'])
def obtener_descuentox_retailer(request):
    """
    Obtener descuentos por retailer
    :return:
    """
    data = request.data

    resultado = ln_descuento.resolver_descuento_tienda(data['fecha_actual'], data['retailer_id'])
    print("")
    return Response(resultado)
