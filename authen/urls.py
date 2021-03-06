from django.urls import path
from . import views
from authen.views import CustomerSignUpView, SupplierSignUpView


urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.select_role, name="select_role"),
    path('register_customer/', CustomerSignUpView.as_view(), name="customer_signup"),
    path('register_supplier/', SupplierSignUpView.as_view(), name="supplier_signup"),
    path('login/', views.login_request, name="login"),
    path('logout/', views.logout_page, name="logout"),
]
