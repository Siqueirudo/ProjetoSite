from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib import messages



def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')

        try:
            # Verifica se o nome de usuário já existe
            if User.objects.filter(username=username).exists():
                messages.error(request, "O nome de usuário já está em uso.", extra_tags='user_error')
                return render(request, 'register.html')

            # Verifica se o e-mail já existe
            if User.objects.filter(email=email).exists():
                messages.error(request, "O e-mail já está em uso.", extra_tags='email_error')
                return render(request, 'register.html')

            # Criação do usuário
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()

            # Autentica e faz login automaticamente
            user = authenticate(request, username=username, password=password1)
            if user is not None:
                login(request, user)
                messages.success(request, "Cadastro realizado e login efetuado com sucesso!")
                return redirect('cloth_list')

            messages.error(request, "Erro ao autenticar o usuário após o registro.")
            return render(request, 'register.html')

        except Exception as e:
            messages.error(request, f"Ocorreu um erro: {e}")
            return render(request, 'register.html')

    return render(request, 'register.html')




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
               # Verifica se o usuário existe
                if not User.objects.filter(username=username).exists():
                    messages.error(request, "Usuário não encontrado.")
                else:
                    messages.error(request, "Senha incorreta.")
        else:
            messages.error(request, "Nome de usuario ou senha invalidos.") 
    else:
        # Inicializando um formulário vazio para requisições GET
        login_form = AuthenticationForm()
    
    return render(request, 'loginn.html', {'login_form': login_form})


def logout_view(request):
    logout(request)
    return redirect('cloth_list')



