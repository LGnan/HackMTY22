from django.contrib import admin
from .models import Donacion, LineaDonacion

# Register your models here.

admin.site.register([Donacion,LineaDonacion])

