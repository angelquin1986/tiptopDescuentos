# serializers.py
from rest_framework import serializers

from motor_descuento.modelo.modelo_descuentos import Disccount


class DisccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Disccount
        fields = ('json_data', 'monto_maximo')


class DisccountSerializer(serializers.Serializer):
    class Meta:
        model = Disccount
        fields = ('json_data', 'monto_maximo', 'monto_actual')
