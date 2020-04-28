# views.py -> account
from django.shortcuts import render


def home(request):
    return render(request, 'account/home.html')


def signup_account(request):
    return render(request, 'account/signup_account.html')


def login_account(request):
    return render(request, 'account/login_account.html')


def logout_account(request):
    return render(request, 'account/logout_account.html')
