"""pi19lanchonete URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from core.views import index, menu, pedido, signup, login, perfil, cadastroPrato, dados, sobre, pratos, excluir, ListaPedidos, cadastroCategoria


urlpatterns = [
	path('index/', index, name='index'),
	path('menu/', menu, name= 'menu'),
	path('pedido/', pedido, name = 'pedido'),
    path('sobre/', sobre, name='sobre'),
    path('perfil/', perfil, name = 'perfil'),
    path('', include('allauth.urls')),
    path('pratos/', pratos, name = 'pratos'),
    path('ListaPedidos/', ListaPedidos, name = 'ListaPedidos'),
    path('cadastroPrato/', cadastroPrato, name = 'cadastroPrato'),
    path('cadastroCategoria/', cadastroCategoria, name = 'cadastroCategoria'),
    path('dados/<int:id>/', dados, name='dados'),
    
    
    path('excluir/<int:id>/', excluir, name="excluir"),
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
