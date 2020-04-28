# views.py -> account
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate


def home(request):
    return render(request, 'account/home.html')


def signup_account(request):
    if request.method == 'GET':
        return render(request, 'account/signup_account.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('aacount:home')
            except IntegrityError:
                return render(request, 'account/signup_account.html', {'form': UserCreationForm(), 'error': 'Username already in use. Please choose a different username.'})

        else:
            print("hello")
            return render(request, 'account/signup_account.html', {'form': UserCreationForm(), 'error': 'Passwords did not match.'})


def login_account(request):
    return render(request, 'account/login_account.html')


def logout_account(request):
    return render(request, 'account/logout_account.html')
