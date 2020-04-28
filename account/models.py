# models.py -> account
from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    address1 = models.CharField(max_length=100, blank=True)
    address2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=2, blank=True)
    zip_code = models.IntegerField(blank=True)
    country = models.CharField(max_length=2, blank=True)
    phone = models.CharField(max_length=15, blank=True)

    # Django User model relationship
    # this model contains first_name, last_name, email, username and persmissions
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
