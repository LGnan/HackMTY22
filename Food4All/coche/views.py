from django.shortcuts import redirect
from .coche import Coche
from donacion.models import Donan
# Create your views here.

def agregar_donan(request, donan_id):
    coche = Coche(request)
    donan = Donan.objects.get(id=donan_id)
    coche.agregar(donan = donan)
    return redirect("Donacion")

def eliminar_donan(request, donan_id):
    coche = Coche(request)
    donan = Donan.objects.get(id=donan_id)
    coche.eliminar(donan = donan)
    return redirect("Donacion")

def restar_donan(request, donan_id):
    coche = Coche(request)
    donan = Donan.objects.get(id=donan_id)
    coche.restar_donan(donan = donan)
    return redirect("Donacion")

def limpiar_coche(request, donan_id):
    coche = Coche(request)
    coche.limpiar_coche()
    return redirect("Donacion")