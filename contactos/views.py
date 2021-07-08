from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse


def home_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('Sign in'))


def login_view(request):
    if request.method == "POST":
        nome = request.POST['nome']
        palavra_passe = request.POST['palavra-passe']
        user = authenticate(request, nome=nome, palavra_passe=palavra_passe)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, "contactos/login.html")

    return render(request, 'contactos/login.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            nome = form.cleaned_data.get('nome')
            palavra_passe = form.cleaned_data.get('palavra_passe')
            user = authenticate(nome=nome, palavra_passe=palavra_passe)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'contactos/registro.html', {'form': form})
