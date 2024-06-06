from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import userRegistrationForm
from django.contrib.auth import logout

# Create your views here.

def register(request):
    if request.method == "POST":
        form = userRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Success! {'username'}, you have created the account!")
            return redirect('login')
    else:
        form = userRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def user_logout(request):
    logout(request)
    return render(request, 'users/logout.html', {})