from django.shortcuts import render, redirect, get_object_or_404
from .forms import CurriculoForm, Curriculo
from django.views.generic import ListView


def index (request):
    #return render(request,'index.html')
    #return render(request, 'novo_index.html')
    curriculos = Curriculo.objects.all
    return render(request, 'listar_curriculos.html', {'curriculos': curriculos})
    #return render(request, 'index.html')

def formulario(request):
    if request.method == 'POST':
        form = CurriculoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/') 
    else:
        form = CurriculoForm()
    return render(request, 'formulario.html', {'form': form})

def listar_curriculos(request):
    curriculos = Curriculo.objects.all
    return render(request, 'listar_curriculos.html', {'curriculos': curriculos})

def detalhes_curriculo(request, pk):
    curriculo = get_object_or_404(Curriculo, pk=pk)
    return render(request, 'curriculo.html', {'curriculo': curriculo})

class CurriculoListView(ListView):
    model = Curriculo
    template_name = 'listar_curriculos.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Curriculo.objects.filter(nome__icontains=query)
        return Curriculo.objects.all()
