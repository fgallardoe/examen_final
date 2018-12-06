from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User



# Create your models here.


class Regione(models.Model):
    region = models.CharField(max_length=30)

    def __str__(self):
        return self.region


class Comuna(models.Model):
    comuna = models.CharField(max_length=30)
    region = models.ForeignKey(Regione, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}-{1}" .format(self.comuna, self.region)


class Tienda(models.Model):
    nom_tienda = models.CharField(max_length=30)
    dir_tienda = models.CharField(max_length=100)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    telefono = models.IntegerField()
    email = models.EmailField(max_length=254)
    jefe_tienda = models.CharField(max_length=80)

    def __str__(self):
        return self.nom_tienda


class Producto(models.Model):
    id_producto = models.PositiveIntegerField(primary_key=True)
    nom_producto = models.CharField(max_length=100)
    desc_producto = models.CharField(max_length=200)
    tipo_producto = models.CharField(max_length=3)
    precio_producto = models.FloatField()

    def __str__(self):
        return "{0}-{1}".format(self.id_producto, self.nom_producto)


class Oferta(models.Model):
    id_oferta = models.AutoField(primary_key=True)
    id_prod = models.ForeignKey(Producto, on_delete=models.CASCADE, blank=True)
    descuento = models.FloatField(default=0)

    def __str__(self):
        return "{0}".format(self.descuento)


class Vendedor(models.Model):
    id_vendedor = models.IntegerField(primary_key=True)
    nom_vendedor = models.CharField(max_length=100)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)

    def __str__(self):
        return  "{0}-{1}".format(self.id_vendedor, self.nom_vendedor)


class Venta(models.Model):
    fecha = models.DateField(auto_now_add=True, blank=True)
    hora = models.TimeField(auto_now_add=True, blank=True)
    cantidad = models.IntegerField(default=0)
    id_prod = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    comentario = models.CharField(max_length=100, blank=True)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE, default=0)
    valor_pesos = models.FloatField(default=0, blank=True)
    descuento = models.ForeignKey(Oferta, on_delete=models.CASCADE, default=0)
    total_pesos = models.FloatField(default=0, blank=True)







