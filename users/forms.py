from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.forms import User
from .models import Customer, Vendor, CustomUser

class userRegistrationForm(UserCreationForm):
    
    is_vendor = forms.BooleanField(required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'is_vendor']

class CustomerUpdateForm(forms.ModelForm):

    #add_money = forms.IntegerField(required=False)

    class Meta:
        model = Customer
        fields = ['add_money']
