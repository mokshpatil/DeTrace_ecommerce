from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView
from .models import Product, Cart, OrderItems, Order
from users.models import CustomUser, Customer, Vendor


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
                    customer.save()

                    for products in cart_items:
                        products.product.quantity -= products.quantity
                        products.product.orders += products.quantity
                        products.product.save()

                    return HttpResponse("order has been placed")
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
    orders = Cart.objects.filter(is_paid=True, user=customer).order_by('-id')

    return render(request, 'store/orderhistory.html', {'orders' : orders})

