from django.urls import path
from . views import *

urlpatterns = [
    path('add-<int:item_id>/', views.add_to_cart, name="add_to_cart"),
    path('cart_view/', views.cart_view, name="cart_view"),
    path('cart_update/<int:cart_item_id>/',
         views.cart_update, name="cart_update"),
    path('empty_cart/', views.empty_cart, name="empty_cart")
]
