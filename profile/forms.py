# forms.py -> account
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('address1', 'address2', 'city', 'state', 'zip_code', 'country', 'phone')

