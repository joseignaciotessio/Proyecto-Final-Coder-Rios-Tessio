from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from users.forms import User_registration_form

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                
                context = {'message':f'Bienvenido {username}!! :D'}
                return render(request, 'index.html', context = context)

        form = AuthenticationForm()
        return render(request, 'users/login.html', {'error': 'Formulário inválido', 'form': form})

    elif request.method == 'GET':
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = User_registration_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            context = {'errors':form.errors}
            form = User_registration_form()
            context['form'] = form
            return render(request, 'users/register.html', context)

    elif request.method == 'GET':
        form = User_registration_form()
        return render(request, 'users/register.html', {'form': form})

def show_profile(request):
    if request.user.is_authenticated:
        return HttpResponse(request.user.profile.address)


@login_required
def edit_user_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            context = {'errors':form.errors}
            form = UserChangeForm()
            context['form'] = form
            return render(request, 'users/register.html', context)

    elif request.method == 'GET':
        form = UserChangeForm()
        return render(request, 'users/register.html', {'form': form})
    
