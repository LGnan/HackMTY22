from django.shortcuts import render
from .models import Donan
# Create your views here.

def donacion(request):
    donaciones = Donan.objects.all()
    return render(request, "donacion/donacion.html",{"donaciones":donaciones})
