from django.db import models
from categories.models import CategoryModel

from django.contrib.auth.models import User


class BookModel(models.Model):
    image = models.ImageField(upload_to='uploads/')
    title = models.CharField(max_length=100)
    category = models.ForeignKey(CategoryModel, related_name="books", on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.PositiveIntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return self.title
    
