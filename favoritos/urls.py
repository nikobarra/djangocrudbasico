from django.urls import path
from .views import *

app_name = "app_favoritos"

urlpatterns = [
    path("", index_favoritos, name="index"),
    path("crear", crear_favoritos, name="crear"),
    path("borrar/<int:pk>", borrar_favoritos, name="borrar"),
    path("detalle/<int:pk>", detalle_favoritos, name="detalle"),
    path("actualizar/<int:pk>", actualizar_favoritos, name="actualizar"),
]
