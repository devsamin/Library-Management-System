from django.db import models
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from accounts.constants import GENDER_TYPE

class UserAccountsModel(models.Model):
    user = models.OneToOneField(User, related_name="accounts", on_delete=models.CASCADE)
    gender = models.CharField(max_length=12, choices=GENDER_TYPE)
    birth_date = models.DateField(null=True, blank=True)
    initial_deposit_date = models.DateField(auto_now_add=True)
    balance = models.DecimalField(default=0, max_digits=14, decimal_places=2)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class UserAddressModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='address')
    street_address = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.user.email}"
