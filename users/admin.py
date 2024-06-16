from django.contrib import admin

from .models import Vendor
from .models import Customer
from .models import CustomUser
from store.models import Product, Cart, OrderItems
from import_export.admin import ImportExportModelAdmin


class OrderItemsAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    ...

admin.site.register(CustomUser)
admin.site.register(Vendor)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Cart)
#admin.site.register(ImportExportModelAdmin)
admin.site.register(OrderItems, OrderItemsAdmin)



# Register your models here.
