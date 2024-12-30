from django.urls import path 
from transactions.views import DepositeView
urlpatterns = [
    path('deposit/', DepositeView.as_view(), name="deposit"),
    
]