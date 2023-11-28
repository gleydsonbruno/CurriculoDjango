from django.db import models

class Curriculo(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    resumo = models.TextField()
    experiencia = models.TextField(default='Sem experiência', null=True)
    formacao = models.TextField()
    habilidades = models.TextField()
    ano = models.IntegerField()
    instituicao = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100, null=True, default='Nunca trabalhei')
    cargo = models.CharField(max_length=100, null=True, default='Sem cargo')
    periodo = models.CharField(max_length=20, null=True, default='0')
    foto = models.ImageField(upload_to='fotos/', blank=True, null=True)

    def __str__(self):
        return f'{self.nome} - Currículo'