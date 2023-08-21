from django.contrib.auth.models import AbstractUser

from django.db import models

class User(AbstractUser):
    age = models.IntegerField(blank=True, null=True)

    # def __str__(self):
    #     return f'user: {self.username}, first_name: {self.first_name}, last_name: {self.last_name}, age: {self.age}'
    def get_user_full_name(self):
        full_name = "$s $s" % (self.first_name, self.last_name)
        return full_name.strip()

    class Meta:
        db_table = 'user'
        verbose_name = "My super user"
        verbose_name_plural = "My super users"