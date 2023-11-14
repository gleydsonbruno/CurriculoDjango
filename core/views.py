from django.shortcuts import render, redirect
from .forms import CurriculoForm, Curriculo

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

def formulario(request):
    if request.method == 'POST':
        form = CurriculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/') 
    else:
        form = CurriculoForm()
    return render(request, 'formulario.html', {'form': form})

def listar_curriculos(request):
    curriculos = Curriculo.objects.all
    return render(request, 'listar_curriculos.html', {'curriculos': curriculos})
