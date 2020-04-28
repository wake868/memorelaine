# models.py -> account
from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address1 = models.CharField(max_length=100, blank=True)
    address2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=2, blank=True)
    zip_code = models.IntegerField(blank=True)
    country = models.CharField(max_length=2, blank=True)
    phone = models.CharField(blank=True)
    email = models.CharField(max_length=75)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(null=True, blank=True)

    # Django User model relationship
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
