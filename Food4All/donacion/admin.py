from django.contrib import admin
from .models import Donan,CategoriaDonan
# Register your models here.
class CategoriaDonanAdmin(admin.ModelAdmin):
    readonly_fields = ("created","updated")
    
class DonanAdmin(admin.ModelAdmin):
    readonly_fields = ("created","updated")
    
admin.site.register(CategoriaDonan , CategoriaDonanAdmin )
admin.site.register(Donan, DonanAdmin)