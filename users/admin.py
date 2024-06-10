from django.contrib import admin

from .models import Vendor
from .models import Customer
from .models import CustomUser

admin.site.register(CustomUser)
admin.site.register(Vendor)
admin.site.register(Customer)

# Register your models here.

#admin pass is passdjango