from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login



def register_view(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            # Salva o usuário sem confirmar o commit
            user = user_form.save(commit=False)
            # Captura o email do POST e atribui ao campo email do usuário
            user.email = request.POST.get('email')
            user.save()  # Agora salva o objeto usuário com o email
            return redirect('cloth_list')  # Redireciona para a página desejada
    else:
        user_form = UserCreationForm()

    return render(request, 'login.html', {'user_form': user_form})

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


