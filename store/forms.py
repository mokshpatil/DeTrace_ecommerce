from django import forms
from .models import Vendor, CustomUser, Review, Product

class VendorUpdateForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['email']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'description']

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'image', 'description', 'price', 'quantity', ]