from django.db import models

class Curriculo(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    resumo = models.TextField()
    experiencia = models.TextField()
    formacao = models.TextField()
    habilidades = models.TextField()

    def __str__(self):
        return f'{self.nome} - Currículo'