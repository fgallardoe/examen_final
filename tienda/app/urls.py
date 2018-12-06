from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name="index"),
    path('productos/', views.inicio, name="inicio"),
    path('productos/crear', views.crear, name="crear"),
    path('listar/', views.listar, name="listar"),
    path('listar/eliminar/<int:id>', views.eliminar, name="eliminar"),


]