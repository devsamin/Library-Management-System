from django import forms
from .models import TransactionModel

class DepositeForm(forms.ModelForm):
    class Meta:
        model = TransactionModel
        fields = ['amount']
    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('account', None)  # account ta pop korteci
        super().__init__(*args, **kwargs)
        
    def save(self, commit = True):
        self.instance.account = self.account
        self.instance.balance_after_transaction = self.account.balance
        return super().save()
    def clean_amount(self):
        min_deposit_amount = 98
        amount = self.cleaned_data.get('amount')
        if amount < min_deposit_amount:
            raise forms.ValidationError(
                f'For you need deposit at least {min_deposit_amount} $'
            )
        return amount