#Archivo para incluir varias urls

from django.urls import path
from . import views

urlpatterns = [

    path('',views.autenticacion, name = "Autenticacion"),
  
]
