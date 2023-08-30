from django.db import models

from book.models import Book
from user.models import User



class Purchase(models.Model):
    # user_id = models.IntegerField(null=False)
    # book_id = models.IntegerField(null=False)
    date = models.DateField(null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    book = models.OneToOneField(Book, on_delete=models.CASCADE)


    class Meta:
        db_table = 'purchase'
        ordering = ('-date',)
        verbose_name = "Purchase list"
        verbose_name_plural = "Purchases list"
