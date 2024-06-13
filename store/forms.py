from django import forms
from .models import Vendor, CustomUser

class VendorUpdateForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['email']
