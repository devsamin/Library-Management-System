from django.urls import path
from .views import BooksDetailsView
urlpatterns = [
    path('details/<int:id>', BooksDetailsView.as_view(), name="details"),
]