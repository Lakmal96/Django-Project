from django.urls import path
from .views import *

urlpatterns = [
    path('', ItemListView.as_view(), name="items"),
    path('<slug:slug>/', views.item_detail, name="item_detail"),

]

# path('<slug:slug>/', ItemDetailView.as_view(), name="detail"),
