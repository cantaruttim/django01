from django.db import models

class Produto(models.Model):
    nome = models.CharField('nome', max_length=100)
    preco = models.DecimalField('preço', decimal_places=2, max_digits=10)
    estoque = models.IntegerField('Quantidade em Estoque')

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField('nome', max_length=100)
    sobrenome = models.CharField('sobre nome', max_length=100)
    email = models.CharField('E-mail', max_length=100)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
