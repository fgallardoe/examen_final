from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Producto
import requests

# Create your views here.


def index(request):
    response = requests.get('http://api.wahrungsrechner.org/v1/quotes/USD/CLP/json?quantity=1&key=1456|pC0POvm952GtJcU8JbZUHa0BO_TqOm7x')
    data = response.json()
    return render(request, 'index.html', {'data': data})


def inicio(request):
    response = requests.get('http://api.wahrungsrechner.org/v1/quotes/USD/CLP/json?quantity=1&key=1456|pC0POvm952GtJcU8JbZUHa0BO_TqOm7x')
    data = response.json()
    return render(request, "productos.html",{'data': data})


def crear(request):
    id_producto = request.POST.get('id_producto', 0)
    nom_producto = request.POST.get('nom_producto', '')
    desc_producto = request.POST.get('desc_producto', '')
    tipo_producto = request.POST.get('tipo_producto', '')
    precio_producto = request.POST.get('precio_producto',0)
    productos = Producto(id_producto=id_producto, nom_producto=nom_producto, desc_producto=desc_producto, tipo_producto=tipo_producto, precio_producto=precio_producto)
    productos.save()
    return render(request,"recibido.html")


def listar(request):
    return render(request, 'listarprod.html', {'elementos':Producto.objects.all()})


def eliminar(request, id):
    productos = Producto.objects.get(pk=id)
    productos.delete()
    return render(request, 'listarprod.html', {'elementos': Producto.objects.all()})

