from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ProductDetailView, ProductCreateView, ProductListView, add_to_cart, placeorder

urlpatterns = [
    path('', ProductListView.as_view(), name='store'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/new/', ProductCreateView.as_view(), name = 'product_create'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('user/', views.user, name='user'),
    path('add-to-cart/<int:id>/', add_to_cart, name="add_to_cart"),
    path('orderplaced/', placeorder, name="orderplaced"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
