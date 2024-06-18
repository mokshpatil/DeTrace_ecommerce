from django.db import models
#from django.contrib.auth.models import User
from users.models import Vendor, Customer, CustomUser
from django.urls import reverse
from decimal import Decimal
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=150, null=True)
    image = models.ImageField(upload_to='prod_pics')
    description = models.TextField(max_length=400, default="")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(default=0)
    orders = models.IntegerField(default=0)
    discount = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(99)])
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})
    
    def get_discounted_price(self):
        if self.discount:
            discount_amount = self.price * Decimal(self.discount / 100)
            discounted_price = self.price - discount_amount
            return round(discounted_price, 2)
        return self.price

class Order(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True)
    date_orderd = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__ (self):
        return str(self.id)
    
class Cart(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)

    def total_value(self):
        total_value = Decimal('0.00')
        for item in self.orderitems_set.all():
            total_value += item.get_discounted_price() * item.quantity
        return total_value


class OrderItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    #order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)

    def get_discounted_price(self):
        return self.product.get_discounted_price()

class Wishlist(models.Model):
    customer = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

class WishlistItems(models.Model):
    wl = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)


class Review(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=250, default='')
    def __str__(self):
        return self.title

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True, null=True)
    vendor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.code

