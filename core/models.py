from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	email = models.CharField('email', max_length=254)
	endereco = 	models.CharField('endereco', max_length = 254)
	ncasa = models.CharField('ncasa', max_length = 6)
	cep = models.CharField('cep', max_length = 8)
	telefone = models.CharField('telefone', max_length = 9)	
	cpf = models.CharField('CPF', max_length = 11)
	foto = models.ImageField('foto', upload_to = 'media/')
	def __str__(self):
		return self.cpf


class categoria(models.Model):
	nome = models.CharField('nome', max_length=100)
	
	def __str__(self):
		return self.nome

class produto(models.Model):
	nome = models.CharField('nome', max_length=100)
	descricao = models.CharField('descricao', max_length=500)
	imagem = models.ImageField('imagem', upload_to='media/', max_length=100)
	preco = models.DecimalField('preco', max_digits=5, decimal_places=2, null = True) 
	categoria = models.ForeignKey(categoria, on_delete=models.CASCADE )

	def __str__(self):
		return self.nome

class pedido(models.Model):
	quantidade = models.IntegerField('quantidade', null=True)
	tempo = models.DateTimeField('tempo', auto_now=True, auto_now_add=False)
	produto = models.ForeignKey(produto, on_delete=models.CASCADE)
	cliente = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	etapa = models.PositiveSmallIntegerField('Etapa', default=0)

	def __str__(self):
		return '%s x %s' % (self.produto, self.quantidade)


	
#class avaliacao(models.Model):
# Create your models here.
