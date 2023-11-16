from django.shortcuts import render

# Create your views here.
# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirecione para sua página principal após o registro
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
