from django.urls import path
from . views import *
# from .views import ItemListView, ItemDetailView

urlpatterns = [
    path('', ItemListView.as_view(), name="items"),
    path('<slug:slug>/<int:id>', views.item_detail, name="detail"),

]
# path('<slug:slug>/', ItemDetailView.as_view(), name="detail"),
