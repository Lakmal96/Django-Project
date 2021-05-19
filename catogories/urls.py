from django.urls import path
from . views import *

urlpatterns = [
    path('', CategoryList.as_view(), name="category_list"),
    path('<int:cat_id>/', views.CategoryView, name="category")
]
