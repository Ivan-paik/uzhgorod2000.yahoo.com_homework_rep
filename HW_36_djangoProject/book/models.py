from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=100, null=False)
    year = models.IntegerField(null=False)
    price = models.IntegerField(null=False)

    class Meta:
        db_table = 'book'
        constraints = [
            models.UniqueConstraint(fields=['title', 'author'], name="%(app_label)s_%(class)s_unique")
        ]
