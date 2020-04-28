# urls.py -> accounts
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.home, name='home'),

    # AUTH
    path('signup/', views.signup_account, name='signup_account'),
    path('login/', views.login_account, name='login_account'),
    path('logout/', views.logout_account, name='logout_account'),
]