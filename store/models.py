from django.db import models
#from django.contrib.auth.models import User
from users.models import Vendor, Customer
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=100, null=True)
    image = models.ImageField(default='',upload_to='prod_pics')
    description = models.TextField(max_length=400, default="")
    price = models.IntegerField()
    seller = models.ForeignKey(Vendor, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(default=0)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})
    

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_orderd = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__ (self):
        return str(self.id)
    
class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def cart_value(self):
        total_value = sum(i.product.price*i.quantity for i in self.orderitems_set.all())
        return total_value


class OrderItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    qunatity = models.IntegerField(default=0, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)

