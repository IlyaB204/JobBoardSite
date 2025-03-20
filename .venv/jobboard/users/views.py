from http.client import HTTPResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import User

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'users/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')


        if User.objects.filter(username = username).exists():
            return HTTPResponse("Пользователь с таким именем уже существует")
        else:
            if password == password2:
                user = User.objects.create_user(username = username,email = email, password=password, first_name = first_name, name = name, last_name = last_name)
                user.save()
                user = authenticate(username = username, password = password)
                login(request, user)
                return redirect('home')
            else:
                return HTTPResponse('Пароли не совпадают')

    return render(request, 'users/register.html')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return render(request, 'users/logout.html')