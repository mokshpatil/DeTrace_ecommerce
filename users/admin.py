from django.contrib import admin

from .models import Vendor
from .models import Customer
from .models import CustomUser
from store.models import Product, Cart, Order

admin.site.register(CustomUser)
admin.site.register(Vendor)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Cart)


# Register your models here.
