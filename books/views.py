from django.shortcuts import render
from django.views.generic import DetailView
from .models import BookModel
from Purchase.forms import ReviewForm
from Purchase.models import PurchaseModel
from django.contrib import messages
from django.shortcuts import render, redirect


class BooksDetailsView(DetailView):
    model = BookModel
    template_name = 'books/details.html'
    pk_url_kwarg = 'id'
    context_object_name = 'book'

    def post(self, *args, **kwargs):
        review_form = ReviewForm(data = self.request.POST)
        book = self.get_object()
        if PurchaseModel.objects.filter(user = self.request.user, book = book).exists():

            if review_form.is_valid():
                new_review = review_form.save(commit=False)
                new_review.book = book
                new_review.user = self.request.user 
                new_review.save()
                messages.success(self.request, "Your review has been successfully added!")  # Success message
                return redirect('details',id=book.id)
        else:
            messages.warning(self.request, "You must purchase this book to leave a review.")
        return self.get(self.request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        book = self.object
        reviews = book.reviews.all()
        review_form = ReviewForm()

        context['book'] = book
        context['reviews'] = reviews
        context['review_form'] = review_form

        return context

