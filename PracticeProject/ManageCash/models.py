from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    def __str__(self):
        return self.username

class AddCash(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True)
    source = models.CharField(max_length=255,null=True)
    datetime = models.DateTimeField(null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    description = models.TextField()
    category = models.CharField(max_length=100, default="addcash",null=True)

class Expense(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField(null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    datetime = models.DateTimeField(null=True)
    category = models.CharField(max_length=100, default="expense",null=True)
