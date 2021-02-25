from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm 

def register(request):
    """Faz cadastro de novo usuario"""
    if request.method != 'POST':
        # Exibe o formulario para cadastro, em branco.
        form = UserCreationForm()
    else:
        # Processa o formulario com os dados preenchidos
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            # Faz login do user e o redireciona para index.
            authenticated_user = authenticate(username=new_user.username, 
            password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)