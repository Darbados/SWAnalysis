from django.contrib import messages
from django.shortcuts import redirect


def index(request):
    messages.info(request, 'Worlds page is in development')
    return redirect('home:index')
