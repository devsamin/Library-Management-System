from django.contrib import admin
from django.urls import path , include
from accounts.views import UserRegistrationView, UserLoginView,UserLogoutView,home,ProfileView
urlpatterns = [
    path('', home, name="homepage"),
    path('category/<slug:slug_id>/', home, name="brand"),
    path('profile', ProfileView.as_view(), name="profilepage"),
    path('registration/', UserRegistrationView.as_view(), name="registration" ),
    path('login/', UserLoginView.as_view(), name="login" ),
    path('logout/', UserLogoutView, name="logout" ),
]