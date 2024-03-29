from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import produto, pedido, categoria, CustomUser

class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = CustomUser

		fields = ('username', 'email', 'endereco', 'ncasa', 'cep', 'telefone', 'cpf', 'foto')

class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = CustomUser
		fields = ('username', 'email', 'endereco', 'ncasa', 'cep', 'telefone', 'cpf', 'foto')

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

