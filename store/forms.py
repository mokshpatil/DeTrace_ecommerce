from django import forms
from .models import Vendor, CustomUser, Review

class VendorUpdateForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['email']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'description']