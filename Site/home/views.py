from django.contrib import messages
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST


def index(request):
    return render(request, 'home/index.html')


@require_POST
def login(request):
    if request.user.is_authenticated:
        messages.info(request, f'User f{request.user.email} is already logged in')
        return redirect('home:index')

    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(email=email, password=password)
    if user is not None:
        django_login(request, user)
        messages.success(request, f'User {request.user.email} logged in')
        return redirect('home:index')
    else:
        messages.error(request, 'User not found')
        return redirect('home:index')


@require_POST
def logout(request):
    django_logout(request)
    return redirect('home:index')
