from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# from . forms import LoginForm, RegisterForm

from . forms import CustomerSignUpForm, SupplierSignUpForm
from . models import User, Customer, Supplier

# Create your views here.


def home(request):
    return render(request, 'authen/home.html', {})


def select_role(request):
    return render(request, 'authen/select_role.html', {})


class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'authen/customer_registration.html'

    # def get_context_data(self, **kwargs):
    #     kwargs['user_type'] = 'customer'
    #     return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('/login')


class SupplierSignUpView(CreateView):
    model = User
    form_class = SupplierSignUpForm
    template_name = 'authen/supplier_registration.html'

    # def get_context_data(self, **kwargs):
    #     kwargs['user_type'] = 'supplier'
    #     return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('/login')


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
                # if user == customer:
                #     return redirect('/')
                # elif user == supplier:
                #     return redirect('/items')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'authen/login.html', context={'form': AuthenticationForm()})


def logout_page(request):
    logout(request)
    return redirect('/')


# def login_page(request):
#     form = LoginForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'authen/login.html', context)


# def registration_page(request):

#     form = RegisterForm()
#     context = {
#         'form': form
#     }
#     if request.method == "POST":
#         print(request.POST.get('name'))
#         print(request.POST.get('address'))
#         print(request.POST.get('email'))
#         print(request.POST.get('phone_number'))
#         print(request.POST.get('role'))
#         print(request.POST.get('username'))
#         print(request.POST.get('password'))
#         print(request.POST.get('password1'))
#     return render(request, 'authen/registration.html', context)
