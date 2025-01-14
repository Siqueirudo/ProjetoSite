from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')

        # Verifica se o usuário já existe
        if User.objects.filter(username=username).exists():
            messages.error(request, "O nome de usuário já está em uso.")
            return render(request, 'register.html')

        # Criação do usuário
        user = User.objects.create_user(username=username, email=email, password=password1)
        messages.success(request, "Cadastro realizado com sucesso! Faça login.")
        return redirect('cloth_list')

    return render(request, 'register.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == "POST":
        # Inicializando o formulário com os dados enviados
        login_form = AuthenticationForm(data=request.POST)
        
        if login_form.is_valid():
            # Extraindo os dados do formulário validado
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            
            # Autenticando o usuário
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                # Usuário autenticado com sucesso
                login(request, user)
                return redirect('cloth_list')
            else:
                # Adicionando uma mensagem de erro personalizada
                login_form.add_error(None, "Usuário ou senha inválidos.")
    else:
        # Inicializando um formulário vazio para requisições GET
        login_form = AuthenticationForm()
    
    return render(request, 'loginn.html', {'login_form': login_form})


