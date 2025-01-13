from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

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
