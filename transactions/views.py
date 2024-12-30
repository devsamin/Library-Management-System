from django.shortcuts import render
from transactions.forms import DepositeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.views import View
from .models import TransactionModel
from django.shortcuts import redirect, get_object_or_404
from Purchase.models import PurchaseModel


def send_email_transaction(user, amount, subject, template):
    message = render_to_string(template, {
        'user' : user,
        'amount' : amount
    })
    to_email = user.email
    send_email = EmailMultiAlternatives(subject, '', to=[to_email])
    send_email.attach_alternative(message, 'text/html')
    send_email.send()

class DepositeView(LoginRequiredMixin, CreateView):
    form_class = DepositeForm
    template_name = 'transactions/deposit.html'
    success_url = reverse_lazy('homepage')
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['account'] = self.request.user.accounts # account pass kore hoccee form e
        return kwargs

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.accounts
        account.balance += amount

        account.save(
            update_fields = ['balance']
        )
        messages.success(self.request, f"{amount}$ was deposit to your account successfully")
        send_email_transaction(self.request.user, amount, "Deposite Message", "transactions/deposit_email.html" )
        return super().form_valid(form)

