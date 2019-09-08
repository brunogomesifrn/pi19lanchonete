from django.forms import ModelForm
from .models import produto

class produtoForm(ModelForm):
	class Meta:
		model = produto
		fields = ['nome', 'preco', 'imagem', 'descricao'] 	