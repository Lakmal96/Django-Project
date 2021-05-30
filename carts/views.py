from django.shortcuts import render, redirect
from . import views

from products.models import Item
from carts.models import Cart, CartItem

# Create your views here.


def add_to_cart(request, item_id):
    item = Item.objects.get(id=item_id)
    # check if cart exists
    cart_id = request.session.get('cart_id', None)
    if cart_id:
        cart_obj = Cart.objects.get(id=cart_id)
        item_in_cart = cart_obj.cartitem_set.filter(item=item)
        # item already in the cart
        if item_in_cart.exists():
            cartitem = item_in_cart.first()
            cartitem.quantity += 1
            cartitem.subtotal += item.selling_price
            cartitem.save()
            cart_obj.total += item.selling_price
            cart_obj.save()
        # new item added to cart
        else:
            cartitem = CartItem.objects.create(
                cart=cart_obj, item=item, unit_price=item.selling_price, quantity=1, subtotal=item.selling_price)
            cart_obj.total += item.selling_price
            cart_obj.save()
    # if cart doesnot exists
    else:
        cart_obj = Cart.objects.create()
        request.session['cart_id'] = cart_obj.id
        cartitem = CartItem.objects.create(
            cart=cart_obj, item=item, unit_price=item.selling_price, quantity=1, subtotal=item.selling_price)
        cart_obj.total += item.selling_price
        cart_obj.save()
    return render(request, 'carts/add_to_cart.html', {'item': item})


def cart_update(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    action = request.GET.get("action")
    cart_obj = cart_item.cart
    if action == "increase":
        cart_item.quantity += 1
        cart_item.subtotal += cart_item.unit_price
        cart_item.save()
        cart_obj.total += cart_item.unit_price
        cart_obj.save()
    elif action == "decrease":
        cart_item.quantity -= 1
        cart_item.subtotal -= cart_item.unit_price
        cart_item.save()
        cart_obj.total -= cart_item.unit_price
        cart_obj.save()
        if cart_item.quantity == 0:
            cart_item.delete()
    elif action == "remove":
        cart_obj.total -= cart_item.subtotal
        cart_obj.save()
        cart_item.delete()
    return redirect("cart_view")


def empty_cart(request):
    cart_id = request.session.get('cart_id', None)
    if cart_id:
        cart = Cart.objects.get(id=cart_id)
        cart.cartitem_set.all().delete()
        cart.total = 0
        cart.save()
    return redirect("cart_view")


def cart_view(request):
    cart_id = request.session.get('cart_id', None)
    if cart_id:
        cart = Cart.objects.get(id=cart_id)
    else:
        cart = None

    return render(request, 'carts/cart_view.html', {'cart': cart})
