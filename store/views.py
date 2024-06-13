from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView
from .models import Product, Cart, OrderItems, Order, WishlistItems, Wishlist
from users.models import CustomUser, Customer, Vendor
import csv
from .forms import VendorUpdateForm
from django.contrib import messages
from mailjet_rest import Client
import os
from dotenv import load_dotenv
load_dotenv(override=True)


API_KEY = os.environ['MJ_APIKEY_PUBLIC']
API_SECRET = os.environ['MJ_APIKEY_PRIVATE']
mailjet = Client(auth=(API_KEY, API_SECRET), version='v3.1')

def store(request):
    context={
        'products' : Product.objects.all()
    }
    return render(request, 'store/store.html', context)

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)

def user(request):
    context = {}
    return render(request, 'store/user.html', context)

class ProductListView(ListView):
    model = Product
    template_name = 'store/store.html'  
    context_object_name = 'products'
    ordering = ['-price']

class ProductDetailView(DetailView):
    model = Product

class ProductCreateView(CreateView):
    model = Product
    fields = ['title', 'image', 'description', 'price', 'quantity']
    

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)
    
@login_required
def add_to_cart(request, id):
    product = Product.objects.get(id=id)
   # customer = request.user
    cart, created = Cart.objects.get_or_create(customer = request.user, is_paid = False)

    cart_item, created = OrderItems.objects.get_or_create(cart=cart, product=product)
    if created:
        cart_item.quantity = 1
        cart_item.save()
        print(f"Added {product} to cart {cart}")
    else:
        cart_item.quantity += 1
        cart_item.save()
        print(f"Updated {product} quantity in cart {cart}")
    return HttpResponseRedirect('/')

@login_required
def add_to_wishlist(request, id):
    product = Product.objects.get(id=id)
    wl, created = Wishlist.objects.get_or_create(customer = request.user)
    wishlist_items, created = WishlistItems.objects.get_or_create(wl = wl, product=product)
    if created:
        wishlist_items.save()
        messages.success(request, f"{product.title} has been added to your wishlist")
    else:
        messages.error(request, f"{product.title} already exists in your wishlist")
    return HttpResponseRedirect('/')


@login_required
def cart(request):
    #customer = request.user
    cart, created = Cart.objects.get_or_create(customer = request.user, is_paid=False)
    cart_items = cart.orderitems_set.all()
    products = [i.product for i in cart_items]

    context = {
        'cart': cart,
        'cart_items': cart_items,
        'products': products
    }

    return render(request, 'store/cart.html', context)

@login_required
def wishlist(request):
    wl, created = Wishlist.objects.get_or_create(customer = request.user)
    wishlist_items = wl.wishlistitems_set.all()
    products = [i.product for i in wishlist_items]

    context = {
        'wishlist': wl,
        'wishlist_items' : wishlist_items,
        'products' : products
    }
    return render(request, 'store/wishlist.html', context)

@login_required
def clearwishlist(request):
    wl = Wishlist.objects.filter(customer = request.user).first()
    wl.delete()
    return redirect('store')

@login_required
def clearcart(request):
    cart = Cart.objects.filter(is_paid=False, customer = request.user).first()
    cart.delete()
    return redirect('store')
    

@login_required
def placeorder(request):
    if request.method == 'POST':
       # customer = request.user
        cart = Cart.objects.filter(is_paid=False, customer = request.user).first()
        customer = CustomUser.objects.filter(username = request.user.username).first()
        cart_items = cart.orderitems_set.all()
        quantityenough = True
        profile = Customer.objects.filter(user = customer).first()
        for products in cart_items:
            if products.product.quantity < products.quantity:
                quantityenough = False
        

        if cart:
            if quantityenough :
        
                if profile.wallet_balance > cart.total_value():
                    cart.is_paid = True
                    cart.save()
                    profile.wallet_balance = profile.wallet_balance - cart.total_value()
                    profile.save()
                    cart_sellers = []
                    for products in cart_items:
                        if not (products.product.seller in cart_sellers):
                            cart_sellers.append(products.product.seller)
                            data = {'Messages': [
                            {
                            "From": {
                                "Email": "mailfortrivialstuff@gmail.com",
                                "Name": "Moksh"
                            },
                            "To": [
                                {
                                "Email": "{products.product.seller.email}",
                                "Name": "{products.product.seller.username}"
                                }
                            ],
                            "Subject": "Update from DeTrace e-commerce!",
                            "TextPart": "Greetings {products.product.seller.username}. An order has been placed for {products.product} of {products.product.quantity} units.!",
                            "HTMLPart": ""
                            }
                        ]
                        }
                            result = mailjet.send.create(data=data)
                            print(result.status_code)
                            print(result.json())
                        products.product.quantity -= products.quantity
                        products.product.orders += products.quantity
                        products.product.save()

                    return render(request, 'store/orderplaced.html')
                else:
                    return HttpResponse("not enough money")
            else:
                cart.delete()
                return HttpResponse("Sorry, please order in available quantity")
        else:
            return redirect('cart')

    return redirect('cart')

@login_required
def orderhistory(request):
    customer = request.user
    orders = Cart.objects.filter(is_paid=True, customer=customer).order_by('id')

    return render(request, 'store/orderhistory.html', {'orders' : orders})

@login_required
def sellerdashboard(request):
    products= Product.objects.filter(seller=request.user)
    return render(request, 'store/sellerdashboard.html', {'products': products})

@login_required
def getreport(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=vendor_report.csv'
    writer = csv.writer(response)
    products = Product.objects.filter(seller = request.user)
    writer.writerow(['Title', 'Price', 'Orders', 'Available'])
    for i in products:
        writer.writerow([i.title, i.price, i.orders, i.quantity])
    return response

@login_required
def vendorupdate(request):
    vendor = CustomUser.objects.filter(username=request.user.username).first()
    #vendor = Vendor.objects.filter(user=customuser).first()
    if request.method == "POST":
        vendor_update = VendorUpdateForm(request.POST, instance=vendor)
        if vendor_update.is_valid():
            vendor_update.save()
            messages.success(request, f"Your e-mail has been successfully changed to {vendor.email}")
    else:
     vendor_update = VendorUpdateForm()
    return render(request, 'store/vendorupdate.html', {'vendor_update':vendor_update})


"""
API_KEY = os.environ['57697d9bf19f182471b769b2ec961ae5']
API_SECRET = os.environ['9b214fd9567baccfc07f6a9cd1329344']
mailjet = Client(auth=(API_KEY, API_SECRET), version='v3.1')
def send_mail(request):
    vendor = request.user
    data = {
  'Messages': [
    {
      "From": {
        "Email": "mailfortrivialstuff@gmail.com",
        "Name": "Moksh"
      },
      "To": [
        {
          "Email": "{vendor.email}",
          "Name": "{vendor.name}"
        }
      ],
      "Subject": "Update from DeTrace e-commerce!",
      "TextPart": "Greetings {vendor.name}. An order has been placed for you listing.!",
      "HTMLPart": ""
    }
  ]
}
    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())
"""