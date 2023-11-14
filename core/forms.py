# resume/forms.py
from django import forms
from .models import Curriculo

class CurriculoForm(forms.ModelForm):
    class Meta:
        model = Curriculo
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Insira o seu nome'}),
            'sobrenome': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Insira o seu sobrenome'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Insira o seu email'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Insira o seu telefone'}),
            'resumo': forms.Textarea(attrs={'class': 'form-group', 'placeholder':'Fale um pouco sobre você'}),
            'experiencia': forms.Textarea(attrs={'class': 'form-group', 'placeholder':'Insira suas experiências trabalhistas'}),
            'formacao': forms.Textarea(attrs={'class': 'form-group', 'placeholder':'Insira sua formação (se tiver)'}),
        }
