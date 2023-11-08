from django.shortcuts import render
from .forms import SolicitacaoCurriculoForm

def index (request):
    
    context = {
        'curso': 'programação web com django e framework'
    }
    return render(request,'index.html')
def curriculo_nat (request):
    return render(request,'curriculo_nat.html')

def curriculo_gley (request):
    return render(request,'curriculo_gley.html')

def curriculo_eliel (request):
    return render(request,'curriculo_eliel.html')

def curriculo_helo (request):
    return render(request,'curriculo_helo.html')

def curriculo_glyc (request):
    return render(request,'curriculo_glyc.html')


def solicitar(request):
    if request.method == 'POST':
        form = SolicitacaoCurriculoForm(request.POST)
        if form.is_valid():
            print('dando certo')

    else:
        form = SolicitacaoCurriculoForm()

    return render(request, 'formulario.html', {'form': form})
