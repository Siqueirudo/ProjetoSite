from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
#from .forms import SimpleUserCreationForm


def register_view(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('register')
    else:
        user_form = UserCreationForm()
    return render(request, 'login.html', {'user_form': user_form})



# Create your views here.
