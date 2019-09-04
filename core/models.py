from django.db import models

class produto(models.Model):
	nome = models.CharField('nome', max_length=100)
	descricao = models.CharField('descricao', max_length=500)
	imagem = models.ImageField('imagem', upload_to='media/', max_length=100)
	preco = models.DecimalField('preco', max_digits=5, decimal_places=2, null = True) 

class categoria(models.Model):
	nome = models.CharField('nome', max_length=100)

#class avaliacao(models.Model):
# Create your models here.
