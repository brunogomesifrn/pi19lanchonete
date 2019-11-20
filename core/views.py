from django.shortcuts import render, redirect
from django.db.models import Sum
from django.forms.models import model_to_dict
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from .models import produto, categoria, pedido, CustomUser
from .forms import produtoForm, categoriaForm, CustomUserChangeForm

def index(request):
    categorias = categoria.objects.all()
    contexto = {
        'categorias': categorias
    }
    return render(request, 'index.html', contexto)

def menu(request):
    return render(request, 'menu.html')

def fazer_pedido(request):
    if not request.user.is_authenticated:
        return redirect('account_login')
    total = 0
    if request.method == 'POST':
        pedidos = {k.strip('pedido-'):int(v) for k, v in request.POST.items() if k.startswith('pedido') and v}
        if not pedidos:
        	return redirect('index')
        for id, quant in pedidos.items():
            p = produto.objects.get(pk=id)
            pedido.objects.create(
                produto=p,
                quantidade=quant,
                cliente=request.user
            )
            total += p.preco * quant
    contexto = {
        'pedidos': pedidos,
        'total': total
        }        
    return render(request, 'pedido.html', contexto)


def ListaPedidos(request):
    pedidos = pedido.objects.filter(cliente=request.user)
    total = pedidos.aggregate(Sum('produto__preco'))
    contexto = {
        'pedidos': pedidos,
        'total': total['produto__preco__sum'],
    }
    return render(request, 'ListaPedidos.html', contexto)


def pedidos(request):
    pedidos = pedido.objects.filter(etapa=0)
    contexto = {
        'pedidos': pedidos
    }
    return render(request, 'pedidos.html', contexto)

def sobre(request):
    return render(request, 'sobre.html')


def pratos(request):
    categorias = categoria.objects.all()
    contexto = {
    'categorias': categorias
    }
    return render(request, 'pratos.html', contexto) 

def signup(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    contexto = {
    'form': form
    }   
    return render(request, 'account/cadastro.html', contexto)

def cadastroPrato(request):
    
    form = produtoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()     
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
    user = CustomUser.objects.get(pk=id)
    form = CustomUserChangeForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('perfil')
    contexto = {
    'form': form
    }
    return render(request, 'account/editardados.html', contexto)

def excluir(request, id):
    p = produto.objects.get(pk=id)
    p.delete()
    return redirect('pratos')

def editar(request, id):
    p = produto.objects.get(pk=id)

    form = produtoForm(request.POST or None, instance=p)

    if form.is_valid():
        form.save()
        return redirect('pratos')

    contexto = {
        'form': form
    }
    return render(request, 'cadastroPrato.html', contexto)
