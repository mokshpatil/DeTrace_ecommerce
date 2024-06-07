from django.db import models
from django.contrib.auth.models import User
from users.models import Vendor, Customer

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(null=True)
    description = models.TextField(max_length=400, null=True)
    price = models.FloatField()
    seller = models.ForeignKey(Vendor, on_delete=models.CASCADE, blank=True, null=True)
#image
    def __str__(self):
        return self. name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_orderd = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__ (self):
        return str(self.id)

class OrderItem (models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    qunatity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

