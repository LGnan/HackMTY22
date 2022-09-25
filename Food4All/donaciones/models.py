
from django.db import models
from django.contrib.auth import get_user_model
from tienda.models import Producto
from django.db.models import F,Sum,FloatField

# Create your models here.

User= get_user_model()

class Donacion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.id
    
    @property
    def total(self):
        return self.lineadonacion_set.aggregate(
            total = Sum(F("precio")*F("cantidad"), output_field = FloatField())
        )["total"]
    
    class Meta:
        db_table ='donaciones'
        verbose_name = 'donacion'
        verbose_name_plural = 'donaciones'
        ordering = ['id']
        
class LineaDonacion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto_id =models.ForeignKey(Producto, on_delete=models.CASCADE)
    donacion_id = models.ForeignKey(Donacion, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return f'{self.cantidad} unidades de {self.producto_id.nombre}'     
    
    class Meta:
        db_table ='lineadonaciones'
        verbose_name = 'Linea Donacion'
        verbose_name_plural = 'Lineas Donaciones'
        ordering = ['id']