from django.forms import ModelForm
from .models import produto, pedido, categoria

class produtoForm(ModelForm):
	class Meta:
		model = produto
		fields = ['nome', 'preco', 'imagem', 'descricao', 'categoria'] 

class pedidoForm(ModelForm):
	class Meta:
		model = pedido
		fields = ['quantidade']

class categoriaForm(ModelForm):
	class Meta:
		model = categoria
		fields = ['nome']

			