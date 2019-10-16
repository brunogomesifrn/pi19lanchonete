from django.db import models

class categoria(models.Model):
	nome = models.CharField('nome', max_length=100)

class produto(models.Model):
	nome = models.CharField('nome', max_length=100)
	descricao = models.CharField('descricao', max_length=500)
	imagem = models.ImageField('imagem', upload_to='media/', max_length=100)
	preco = models.DecimalField('preco', max_digits=5, decimal_places=2, null = True) 
	categoria = models.ForeignKey(categoria, on_delete=models.CASCADE )


class pedido(models.Model):
	quantidade = models.IntegerField('quantidade', null=True)
	tempo = models.DateTimeField('tempo', auto_now=True, auto_now_add=False)

#class avaliacao(models.Model):
# Create your models here.
