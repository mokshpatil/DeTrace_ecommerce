from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

class userRegistrationForm(UserCreationForm):
    emaiil = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']