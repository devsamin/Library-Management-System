from django.db import models
from accounts.models import UserAccountsModel
class TransactionModel(models.Model):
    account = models.ForeignKey(UserAccountsModel, related_name="transactions", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    balance_after_transaction = models.DecimalField(max_digits=12, decimal_places=2)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction for {self.account.user} at {self.time_stamp}"