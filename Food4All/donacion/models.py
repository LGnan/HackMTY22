from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models

# Create your models here.

class CategoriaDonan(models.Model):
    nombre = models.CharField(max_length = 50)
    created = models.DateTimeField( auto_now_add = True)
    updated = models.DateTimeField( auto_now_add = True)
    
    class Meta: 
        verbose_name = "categoriaDonan"
        verbose_name_plural = "categoriasDonan"
        
    def _str_(self):
        return self.nombre
    

class Donan(models.Model):
    nombre = models.CharField(max_length = 50)
    categorias = models.ForeignKey(CategoriaDonan, on_delete= models.CASCADE)
    imagen = models.ImageField(upload_to = "donacion", null = True, blank = True )
    disponibilidad = models.BooleanField(default = True )
    created = models.DateTimeField( auto_now_add = True)
    updated = models.DateTimeField( auto_now_add = True) 
    
    class Meta:
        verbose_name = "Donan"
        verbose_name_plural = "Donans"
