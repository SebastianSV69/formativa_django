from django.contrib import admin
from negocio.models import Destino, PaqueteTuristico

@admin.register(Destino)
class DestinoAdmin(admin.ModelAdmin):
    list_display=('nombre','boletos','monto')
    list_filter=('nombre','boletos','monto')
    search_fields = ('nombre','boletos','monto')

@admin.register(PaqueteTuristico)
class PaqueteTuristicoAdmin(admin.ModelAdmin):
    list_display=('nombre','idavuelta','monto','destino')
    list_filter=('nombre','idavuelta','monto','destino')
    search_fields = ('nombre','idavuelta','monto','destino')

