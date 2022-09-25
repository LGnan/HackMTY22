from django.shortcuts import render,redirect

from donaciones.models import Donacion, LineaDonacion
from django.contrib.auth.decorators import login_required
from carro.carro import Carro
from django.contrib import messages
# Create your views here.

@login_required(login_url="/autenticacion/logear")

def procesar_pedido(request):
    pedido = Donacion.objects.create(user=request.user)
    carro= Carro(request)
    lineas_pedidos=list()
    for key,value in carro.carro.items():
        lineas_pedidos.append(LineaDonacion(
            producto_id = key,
            cantidad = value["cantidad"],
            user = request.user,
            pedido= pedido
        ))
            
    LineaDonacion.objects.bulk_create(lineas_pedidos)
    
    enviar_mail(
        pedido = pedido,
        lineas_pedidos = lineas_pedidos,
        nombreusuario = request.username,
        emaulusuario = request.usermail
        
    )
    messages.sucess(request, "El pedido se ha creado correctamente")

    return redirect("../tienda")

def enviar_mail(**kwargs):
    asunto = "Gracias por el pedido"
    mensaje = render_to_string