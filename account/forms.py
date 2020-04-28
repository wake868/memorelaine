# forms.py -> account
from django.forms import ModelForm
from .models import Account

class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = [
            'first_name',
            'last_name',
            'address1',
            'address2',
            'city',
            'state',
            'zip_code',
            'country',
            'phone',
            'email',
        ]

