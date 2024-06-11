from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DeleteView, CreateView
from .models import Product


def store(request):
    context={}
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
    #ordering = ['-orders']

class ProductDetailView(DeleteView):
    model = Product

class ProductCreateView(CreateView):
    model = Product
    fields = ['title', 'image', 'description', 'price', 'quantity']

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)