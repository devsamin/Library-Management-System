
from books.models import BookModel
from .models import PurchaseModel
from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.models import UserAccountsModel
from django.contrib.auth.mixins import LoginRequiredMixin
from transactions.models import TransactionModel
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.views import View
from .models import TransactionModel
from django.shortcuts import redirect, get_object_or_404
from Purchase.models import PurchaseModel




def send_email_transaction(user, book_name, After_balance_transaction,subject, template):
    message = render_to_string(template, {
        'user' : user,
        'After_balance_transaction' : After_balance_transaction,
        'book_name' : book_name,
    })
    to_email = user.email
    send_email = EmailMultiAlternatives(subject, '', to=[to_email])
    send_email.attach_alternative(message, 'text/html')
    send_email.send()

def BuyBookview(request, id):
    book = BookModel.objects.get(id = id)
    try:
        user_account = request.user.accounts # user account er instance
    except UserAccountsModel.DoesNotExist:
        messages.warning(request, "You don't have an account associated. Please create one.")
        return redirect('homepage')
    # print(user_account.username)
    user_balance = user_account.balance
    # print(user_balance)
    book_price = book.price
    if book.quantity > 0:
        if user_balance >= book_price:
            user_account.balance-=book_price
            book.quantity-= 1

            user_account.save()
            book.save()

            trnasaction = TransactionModel.objects.create(account = user_account, amount = book_price, balance_after_transaction = user_account.balance)
            
            PurchaseModel.objects.create(user = request.user, book = book, transaction = trnasaction)

            send_email_transaction(request.user, book.title, trnasaction.balance_after_transaction, "Purchase Message", 'transactions/parchase_email.html')
            messages.success(request, f'You have successfully purchased book {book.title}!')
    else:
        messages.warning(request, f'Sorry, {book.title} book is out of stock!')
    return redirect('homepage')

class PayView(View):
    def get(self, request, pay_id, *args, **kwargs):
        # transaction koje ber 
        print(pay_id)
        purchase = get_object_or_404(PurchaseModel, id=pay_id)
        print(purchase.book)
        if purchase.transaction:
            book = purchase.book
            request.user.accounts.balance += book.price
            # print(request.user.accounts.balance)
            request.user.accounts.save()
            purchase.transaction.delete()
            purchase.delete()

            send_email_transaction(request.user, book.title, purchase.transaction.balance_after_transaction,"Return Book", 'transactions/return_book_email.html')
            messages.success(request, "Book Return Completed, And Balance Update SuccessFully!!")
        else:
            messages.error(request, "No purchase associated with this transaction.")

        return redirect('profilepage')