from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import userRegistrationForm, CustomerUpdateForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

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

@login_required
def myaccount(request):
    if request.method == "POST":
      customer_update = CustomerUpdateForm(request.POST, instance=request.user.customer)
      if customer_update.is_valid():
          customer_update.save()
          messages.success(request, f"Success! {'username'}, your account has been updated!")
          return redirect('myaccount')
        
        
    
    else:
        customer_update = CustomerUpdateForm(instance=request.user.customer)

    context = {
        'customer_update':customer_update,
    }
    return render(request, 'users/myaccount.html', context)