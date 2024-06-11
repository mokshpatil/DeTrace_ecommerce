from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='store'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('product/new/', views.ProductCreateView.as_view(), name = 'product_create'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('user/', views.user, name='user'),
]

