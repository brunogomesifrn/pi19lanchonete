from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# from cart.cart import Cart
from .models import produto, categoria, pedido
from .forms import produtoForm, categoriaForm

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
    if request.method == 'POST':
        pedidos = {k.strip('pedido-'):int(v) for k, v in request.POST.items() if k.startswith('pedido') and v}
        for id, quant in pedidos.items():
            p = produto.objects.get(pk=id)
            pedido.objects.create(
                produto=p,
                quantidade=quant,
                cliente=request.user
            )
        breakpoint()

    return render(request, 'pedido.html')


def pedidos(request):
    pedidos = pedido.objects.filter(etapa=0)
    contexto = {
        'pedidos': pedidos
    }
    return render(request, 'pedidos.html', contexto)

def sobre(request):
    return render(request, 'sobre.html')

def ListaPedidos(request):
    return render(request, 'ListaPedidos.html') 

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

# def adicionar_ao_carrinho(request, produto_id, quantidade):
#     produto = Produto.objects.get(id=produto_id)
#     carrinho = Cart(request)
#     carrinho.add(product, produto.preco, quantidade)
#     return render(request, '')

# def remover_do_carrrinho(request, produto_id):
#     produto = Produto.objects.get(id=produto_id)
#     carrinho = Cart(request)
#     carrinho.remove(produto)
#     return render(request, '')

# def carrinho(request):
#     contexto = {
#         'carrinho': Cart(request)
#     }
#     return render(request, 'cart.html', contexto)
