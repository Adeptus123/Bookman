from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    job=models.TextField(max_length=20)

class Book(models.Model):
    bname=models.TextField(max_length=30)
    bdesc=models.TextField(max_length=100)
    bdate=models.DateTimeField()
    bowner=models.TextField(max_length=30)

    def __str__(self):
        return self.bname
    