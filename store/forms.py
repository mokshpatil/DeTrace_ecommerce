from django import forms
from .models import Vendor, CustomUser, Review, Coupon

class VendorUpdateForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['email']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'description']

class CouponForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = ['code', 'discount', 'is_active']