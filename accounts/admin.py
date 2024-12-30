from django.contrib import admin
from accounts.models import UserAccountsModel, UserAddressModel

admin.site.register(UserAccountsModel)
admin.site.register(UserAddressModel)