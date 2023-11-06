from django.shortcuts import render

def index (request):
    
    context = {
        'curso': 'programação web com django e framework'
    }
    return render(request,'index.html')
def contato (request):
    return render(request,'contato.html')
