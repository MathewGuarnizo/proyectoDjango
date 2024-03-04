"""
URL configuration for primerProyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# from miApp import views #importa las vistas de mi app
import miApp.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('holaMundo/', miApp.views.holaMundo, name="holaMundo"),
    path('saludo/', miApp.views.saludo, name="saludo"),
    path('saludo/<int:redirigir>', miApp.views.saludo, name="saludo"),
    path('', miApp.views.index, name="index"),
    path('presentacion/', miApp.views.presentacion, name="presentacion"),
    path('contactanos/', miApp.views.contactanos, name="contactanos"),
    path('contacto/', miApp.views.contacto, name="contacto"),
    path('contacto/<str:nombre>', miApp.views.contacto, name="contacto"),
    path('contacto/<str:nombre>/<str:apellido>', miApp.views.contacto, name="contacto"),
    path('quienesSomos/', miApp.views.quienesSomos, name="quienesSomos"),
    path('productos_Servicios/', miApp.views.productos_Servicios, name="productos_Servicios"),
    path('crear_articulo/', miApp.views.crearArticulo, name="CrearArticulo"),
    path('crear_articulo/<str:title>/<str:content>/<str:public>', miApp.views.crearArticulo, name="CrearArticulo"),
    path('articulo/', miApp.views.articulo, name="articulo"),
    path('editar_articulo/<int:id>', miApp.views.editar_articulo, name="editarArticulo"),
    path('articulos/', miApp.views.articulos, name="Listar"),
    path('eliminar_articulo', miApp.views.eliminar_articulo, name="eleminarArticulo"),
]