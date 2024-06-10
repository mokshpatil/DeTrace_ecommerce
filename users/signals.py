from .models import Vendor, Customer, CustomUser
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_vendor == False:
            Customer.objects.create(user=instance)
        else:
            Vendor.objects.create(user=instance)
      


"""
@receiver(post_save, sender=User)
def save_customer_profile(sender, instance, created, **kwargs):
    instance.customer.save()
"""