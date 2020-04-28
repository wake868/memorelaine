# urls.py -> accounts
from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/', views.detail, name='detail'),

    # AUTH
    path('signup/', views.create_user, name='create_user'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
]