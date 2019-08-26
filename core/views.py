from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def index(request):
	return render(request, 'index.html')

def menu(request):
	return render(request, 'menu.html')

def pedido(request):
	return render(request, 'pedido.html')

def cadastro(request):
	form = UserCreationForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('login')
	contexto = {
	'form': form
	}	
	return render(request, 'registration/cadastro.html', contexto)

def login(request):
	return render(request, 'login.html')

@login_required
def perfil(request):
	return render(request, 'perfil.html')

