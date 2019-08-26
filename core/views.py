from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
	return render(request, 'index.html')

def menu(request):
	return render(request, 'menu.html')

def pedido(request):
	return render(request, 'pedido.html')

def cadastro(request):
	return render(request, 'cadastro.html')

def login(request):
	return render(request, 'login.html')

@login_required
def perfil(request):
	return render(request, 'perfil.html')

