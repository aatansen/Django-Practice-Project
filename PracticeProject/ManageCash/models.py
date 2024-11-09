from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    def __str__(self):
        return self.username

class AddCash(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    source = models.CharField(max_length=255)
    datetime = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

class Expense(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    datetime = models.DateTimeField()
