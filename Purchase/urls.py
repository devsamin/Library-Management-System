from django.urls import path
from .views import BuyBookview,PayView

urlpatterns = [
    path('buybook/<int:id>/',BuyBookview, name="buybook"),
    path('return_book/<int:pay_id>/', PayView.as_view(), name="return_book"),
]