#Archivo para incluir varias urls

from django.urls import path
from . import views

urlpatterns = [
    path('tienda',views.tienda, name = "Tienda"),

]
