#Archivo para incluir varias urls

from django.urls import path
from . import views

app_name = "coche"

urlpatterns = [
    path('agregar/<int:donan_id>',views.agregar_donan, name = "agregar"),
    path('eliminar/<int:donan_id>',views.eliminar_donan, name = "eliminar"),
    path('restar/<int:donan_id>',views.restar_donan, name = "restar"),
    path('limpiar/<int:donan_id>',views.limpiar_coche, name = "limpiar"),

]
