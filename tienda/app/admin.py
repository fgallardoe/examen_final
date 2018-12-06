from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Regione, Comuna, Producto, Venta, Oferta, Tienda, Vendedor

# Register your models here.
admin.site.site_header = "Admin MiTienda"


class RegistroProducto(admin.ModelAdmin):
    list_display = ('id_producto', 'nom_producto','desc_producto','tipo_producto','precio_producto')
    list_filter = ('id_producto',)
    ordering = ('id_producto',)
    search_fields = ('id_producto',)


class RegistroOferta(admin.ModelAdmin):
    list_display = ('id_oferta','id_prod','descuento')
    list_filter = ('id_oferta',)
    ordering = ('pk',)
    search_fields = ('id_prod',)


class RegistroTienda(admin.ModelAdmin):
    list_display = ('pk', 'nom_tienda','dir_tienda','comuna','telefono','email','jefe_tienda')
    list_filter = ('nom_tienda',)
    ordering = ('pk',)
    search_fields = ('nom_tienda',)



class RegistroVentaFinal(admin.ModelAdmin):
    list_display = ('pk', 'fecha','hora','cantidad','id_prod','tienda','comentario','vendedor','valor_pesos','descuento','total_pesos')
    list_filter = ('id_prod','vendedor','tienda')
    ordering = ('pk',)
    search_fields = ('id_prod',)


admin.site.register(Regione)
admin.site.register(Comuna)
admin.site.register(Producto, RegistroProducto )
admin.site.register(Venta,RegistroVentaFinal)
admin.site.register(Oferta, RegistroOferta)
admin.site.register(Tienda, RegistroTienda)
admin.site.register(Vendedor)

