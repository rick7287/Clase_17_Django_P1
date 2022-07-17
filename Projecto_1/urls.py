"""Projecto_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from Projecto_1.views import saludar, segunda_vista, dia_de_hoy, saludo_con_nombre, calcular_nacimiento, probando_html

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludar, name='saludar'),
    path('segunda/', segunda_vista, name='segunda_vista'),
    path('hoy/', dia_de_hoy, name='dia_de_hoy'),
    path('saludo_con_nombre/<nombre>', saludo_con_nombre, name = 'saludo_con_nombre'),
    path('calcular_nacimiento/<age>', calcular_nacimiento, name = 'calcular_nacimiento'),
    path('probando_html/', probando_html, name = 'probando_html')
]
