from django.shortcuts import render,redirect
from django.views.generic import FormView
from django.contrib.auth.views import LoginView, LogoutView
from accounts.forms import UserRegistrationForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from books.models import BookModel, CategoryModel
from django.contrib import messages
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from Purchase.models import PurchaseModel



def home(request, slug_id = None):
    data = BookModel.objects.all()
    if slug_id is not None:
        book_category = CategoryModel.objects.get(slug = slug_id)
        data = BookModel.objects.filter(category = book_category)

    categorys = CategoryModel.objects.all()
    return render(request, 'accounts/home.html', {'data' : data, 'categorys' : categorys})

class ProfileView(LoginRequiredMixin, ListView):
    template_name = 'accounts/profile.html'
    context_object_name = 'purchace_book'

    def get_queryset(self):
        return PurchaseModel.objects.filter(user = self.request.user)

class UserRegistrationView(FormView):
    template_name = 'accounts/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        user = form.save()
        username = form.cleaned_data['username']
        print(username)
        messages.success(self.request, f"{username} login successfully!!")
        login(self.request, user)
        return super().form_valid(form)

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    def get_success_url(self):
        return reverse_lazy('homepage')
    
def UserLogoutView(request):
    logout(request)
    return redirect('login')

