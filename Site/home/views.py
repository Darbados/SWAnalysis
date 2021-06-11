from django.contrib import messages
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from home.forms import RegisterForm


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


@login_required
@require_POST
def logout(request):
    django_logout(request)
    return redirect('home:index')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            django_login(request, user)
            messages.success(request, f'User {user.email} successfully registered')
            return redirect('home:index')
        else:
            messages.error(request, 'User with given email already exists')
    else:
        form = RegisterForm(request.GET or None)

    data = {'form': form}
    return render(request, 'home/register.html', data)
