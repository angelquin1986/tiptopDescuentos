# motor_descuento/urls.py
from django.conf.urls import url
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'disccount', views.DisccountViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('retailer/list', views.retailer_list, name='index'),
    url('calcular-descuento', views.obtener_descuento, name='calcular-descuento'),
    url('descuento-retailer', views.obtener_descuentox_retailer, name='calcular-descuento-retailer'),
    path('descuentos', TemplateView.as_view(template_name='descuentos.html')),

    # APIS para Front DESCUENTOS
    url('descuentos/get/all', views.descuentos_list, name='index'),

]
