from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import userRegistrationForm, CustomerUpdateForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Customer

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
    customuser = CustomUser.objects.filter(username=request.user.username).first()
    customer = Customer.objects.filter(user=customuser).first()
    
    if request.method == "POST":
        customer_update = CustomerUpdateForm(request.POST, instance=customer)
        if customer_update.is_valid():
            if customer.add_money < 0:
                messages.error(request, f"amount added should be greater than 0")
            customer.wallet_balance += customer.add_money
            customer_update.save()
            messages.success(request, f"Success! {request.user.username}, ${customer.add_money} has been added to your wallet. Your balance is now ${customer.wallet_balance}.")
            return redirect('myaccount')
    else:
        customer_update = CustomerUpdateForm(instance=customer)

    context = {
        'customer_update': customer_update,
    }
    return render(request, 'users/myaccount.html', context)
