from django.db import models

from authen.models import Customer
from products.models import Item

# Create your models here.


class Cart(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Cart : " + str(self.id)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    unit_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    quantity = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return "Cart : " + str(self.cart.id) + " Item : " + str(self.item.name)
