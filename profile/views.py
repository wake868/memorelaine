# views.py -> account
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import ProfileForm, UserForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'profile/home.html')

@login_required
def detail(request):
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile/detail.html', {'user_form': user_form, 'profile_form': profile_form})


def create_user(request):
    if request.method == 'GET':
        return render(request, 'profile/create_user.html', {'user_form': UserForm()})
    else:
        if request.POST['password'] == request.POST['password_check']:
            try:
                new_user = User.objects.create_user(
                    username=request.POST['username'],
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    email=request.POST['email'], 
                    password=request.POST['password'])
                new_user.save()
                login(request, new_user)
                return redirect('profile:detail')
            except IntegrityError:
                return render(request, 'profile/create_user.html', {'user_form': UserForm(), 'error': 'Username already in use. Please choose a different username.'})
        else:
            print("hello")
            return render(request, 'profile/create_user.html', {'user_form': UserForm(), 'error': 'Passwords did not match.'})

def create_profile(request):
    if request.method == 'GET':
        return render(request, 'profile/create_profile.html', {'profile_form': ProfileForm()})
    else:
        form = ProfileForm(request.POST)
        new_profile = form.save(commit=False)
        new_profile.owner = request.user
        new_profile.save()
        return redirect('memorywall:home')


def login_user(request):
    if request.method == 'GET':
        return render(request, 'profile/login_user.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'profile/login_user.html', {'form': AuthenticationForm(), 'error': 'Username or password is invalid.'})
        else:
            login(request, user)
            return redirect('profile:home')


@login_required
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('profile:home')
