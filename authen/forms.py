from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from . models import Customer, Supplier, User


class CustomerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    address = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    # to make sure all operations are done in a single databaase transaction
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        customer = Customer.objects.create(user=user)
        customer.phone_number = self.cleaned_data.get('phone_number')
        customer.address = self.cleaned_data.get('address')
        customer.save()
        return user


class SupplierSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    address = forms.CharField(required=True)
    company_name = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    # to make sure all operations are done in a single databaase transaction
    def save(self):
        user = super().save(commit=False)
        user.is_supplier = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        supplier = Supplier.objects.create(user=user)
        supplier.phone_number = self.cleaned_data.get('phone_number')
        supplier.address = self.cleaned_data.get('address')
        supplier.company_name = self.cleaned_data.get('company_name')
        supplier.save()
        return user


# class LoginForm(forms.Form):
#     CHOICES = (('', '---Please Select the Role---'),
#                ('customer', 'Customer'), ('supplier', 'Supplier'))
#     username = forms.CharField(widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Username'}))
#     password = forms.CharField(widget=forms.PasswordInput(
#         attrs={'class': 'form-control', 'placeholder': 'Password'}))
#     role = forms.ChoiceField(choices=CHOICES, widget=forms.Select(
#         attrs={'class': 'form-control'}))


# class RegisterForm(forms.Form):
#     CHOICES = (('', '---Please Select the Role---'),
#                ('customer', 'Customer'), ('supplier', 'Supplier'))
#     name = forms.CharField(widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Name'}))
#     address = forms.CharField(widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Address'}))
#     email = forms.EmailField(widget=forms.EmailInput(
#         attrs={'class': 'form-control', 'placeholder': 'Email'}))
#     phone_number = forms.CharField(widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Phone Number'}))
#     role = forms.ChoiceField(choices=CHOICES, widget=forms.Select(
#         attrs={'class': 'form-control'}))
#     username = forms.CharField(widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Username'}))
#     password = forms.CharField(widget=forms.PasswordInput(
#         attrs={'class': 'form-control', 'placeholder': 'Password'}))
#     password1 = forms.CharField(widget=forms.PasswordInput(
#         attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}), label='Confirm Password')
