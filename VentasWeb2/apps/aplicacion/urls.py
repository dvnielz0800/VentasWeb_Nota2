from django.conf.urls import url
from .views import *

urlpatterns =[
 	url(r'^$',home,name = "index"),
 	url(r'^inicio/',inicio,name = "inicio"),
 	url(r'^crear_cliente/', CreateCliente.as_view(), name = "crear_cliente"),
 	url(r'^listar_cliente/', ListCliente.as_view(), name = "listar_cliente"),
 	url(r'^editar_cliente/(?P<pk>\d+)/', UpdateCliente.as_view(), name = "editar_cliente"),
 	url(r'^eliminar_cliente/(?P<pk>\d+)/', DeleteCliente.as_view(), name = "eliminar_cliente"),

]