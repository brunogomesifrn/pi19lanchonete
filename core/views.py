from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import produto
from .forms import produtoForm, categoriaForm

def index(request):
	pedido = produto.objects.all()
	contexto = {
		'pedido_lista': pedido
	}
	return render(request, 'index.html', contexto)

def menu(request):
	return render(request, 'menu.html')

def pedido(request):
	return render(request, 'pedido.html')

def sobre(request):
	return render(request, 'sobre.html')

def ListaPedidos(request):
	return render(request, 'ListaPedidos.html')	

def pratos(request):
	pedido = produto.objects.all()
	contexto = {
	'pedido_lista': pedido
	}
	return render(request, 'pratos.html', contexto)	

def cadastro(request):
	form = UserCreationForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('login')
	contexto = {
	'form': form
	}	
	return render(request, 'registration/cadastro.html', contexto)

def cadastroPrato(request):
	
	form = produtoForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		produto = form.save(commit=False)		
		produto.save()
		return redirect('perfil')		
	contexto = {
		'form': form
	}
	
	return render(request, 'cadastroPrato.html', contexto)

def cadastroCategoria(request):
	
	form = categoriaForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		categoria = form.save(commit=False)		
		categoria.save()
		return redirect('perfil')		
	contexto = {
		'form': form
	}
	
	return render(request, 'cadastroCategoria.html', contexto)	

def login(request):
	return render(request, 'login.html')

@login_required
def perfil(request):
	return render(request, 'perfil.html')

@login_required
def dados(request, id):
	user = User.objects.get(pk=id)
	form = UserCreationForm(request.POST or None, instance=user)
	if form.is_valid():
		form.save()
		return redirect('perfil')
		contexto = {
		'form': form
		}
		return render(request, 'registro.html', contexto)

def excluir(request, id):
	pedido = produto.objects.get(pk=id)
	produto.delete()
	return redirect('perfil')