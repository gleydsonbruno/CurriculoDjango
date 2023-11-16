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
    ano = models.IntegerField()
    instituicao = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    periodo = models.CharField(max_length=20)
    foto = models.ImageField(upload_to='fotos/', blank=True, null=True)

    def __str__(self):
        return f'{self.nome} - Currículo'