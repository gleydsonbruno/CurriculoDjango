from django.db import models
from django import forms

class Produto(models.Model):
    nome = models.CharField ('nome', max_length= 100)
    preco = models.DecimalField ('Preço', decimal_places=2,max_digits=8)
    estoque = models.IntegerField('Quantidade no estoque')

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField('nome', max_length=100)
    sobrenome = models.CharField('sobrenome', max_length=100)
    email = models.EmailField('email', max_length=100)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class Curriculo(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    endereco = models.TextField()
    resumo = models.TextField()
    experiencia = models.TextField()
    educacao = models.TextField()

    def __str__(self):
        return f'{self.nome} - Currículo'