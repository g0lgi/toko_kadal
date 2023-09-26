from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, name='name')
    amount = models.IntegerField(name='amount')
    price = models.FloatField(name='price')
    date_added = models.DateTimeField(name='date_added', auto_now_add=True)
    description = models.TextField(max_length=256, name='description')

