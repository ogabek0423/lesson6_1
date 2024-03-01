from django.shortcuts import render


def logins(request):
    return render(request, 'users/login.html')
# Create your views here.


def landing(request):
    return render(request, 'users/landing.html')


def register(request):
    return render(request, 'users/register.html')