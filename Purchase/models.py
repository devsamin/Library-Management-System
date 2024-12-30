from django.db import models
from books.models import BookModel
from django.contrib.auth.models import User
from transactions.models import TransactionModel

class PurchaseModel(models.Model):
    user = models.ForeignKey(User, related_name="purchase", on_delete=models.CASCADE)
    book = models.ForeignKey(BookModel, related_name="purchase_by", on_delete=models.CASCADE)
    transaction = models.OneToOneField(TransactionModel, on_delete=models.CASCADE, related_name="purchase", blank=True,null=True) # potita purchase er ekta trnasaction takbe
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} purchased {self.book.title}"
    
class ReviewModel(models.Model):
    user = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)
    book = models.ForeignKey(BookModel, related_name="reviews", on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} {self.book.title} {self.rating}"
