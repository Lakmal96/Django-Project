from django.urls import path
from . import views

urlpatterns = [
    path('', views.customized_order, name="customized")
]
