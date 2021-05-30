from django.urls import path
<<<<<<< HEAD
from .views import *

urlpatterns = [
    path('', ItemListView.as_view(), name="items"),
    path('<slug:slug>/', views.item_detail, name="item_detail"),

]

=======
from . views import *
# from .views import ItemListView, ItemDetailView

urlpatterns = [
    path('', ItemListView.as_view(), name="items"),
    path('<slug:slug>/<int:id>', views.item_detail, name="detail"),

]
>>>>>>> e3e133833a4b7782be97c8884b89e5fab0d26d75
# path('<slug:slug>/', ItemDetailView.as_view(), name="detail"),
