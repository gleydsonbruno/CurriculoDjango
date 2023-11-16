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
            'resumo': forms.TextInput(attrs={'class': 'form-group', 'placeholder':'Fale um pouco sobre você'}),
            'experiencia': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Insira suas experiências trabalhistas'}),
            'formacao': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Insira sua formação (se tiver)'}),
            'habilidades': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Insira suas habilidades (HTML, CSS, Python, Flutter, etc.)'}),
            'ano': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ano de conclusão'}),
            'instituicao': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nome ou SIGLA da Instituição'}),
            'empresa': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nome da empresa'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Cargo que exercia'}),
            'periodo': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Tempo que passou na empresa'}),
             'foto': forms.ClearableFileInput(),

        }
