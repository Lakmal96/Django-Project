from django.urls import path
from .views import ItemListView, ItemDetailView

urlpatterns = [
    path('', ItemListView.as_view(), name="items"),
    path('<slug:slug>/', ItemDetailView.as_view(), name="detail"),
]
