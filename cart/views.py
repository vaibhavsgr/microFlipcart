from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.utils import timezone

from .forms import OrderForm
from usermgmt.models import Product
from .models import Order



def view_cart(request):
    return render(request, "cart.html")


def thankyou(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        city = request.POST.get('city', '')
        phone = request.POST.get('phone', '')
        status = request.POST.get('status', '')

        cart = request.session.get('cart', {})
        items = {}
        for id, quantity in cart.items():
            product = get_object_or_404(Product, pk=id)
            items[product.name] = product.price


        order = Order(items_json= items, full_name=name, town_or_city=city, phone_number=phone, status=status)
        order.save()
        request.session['cart'] = {}
        id = order.order_id
        return render(request, 'thankyou.html', {'id':id,})
    #return render(request, "thankyou.html")


def add_to_cart(request, id):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)
    request.session['cart'] = cart
    return redirect(reverse('home'))
    #return render(request, "cart.html")


def adjust_cart(request, id):
    quantity=int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


@login_required()
def checkout(request):
    return render(request, 'checkout.html')
        #order_form = OrderForm(request.POST)
        #if order_form.is_valid():
        #    order = order_form.save(commit=False)
        #    order.date = timezone.now()
        #    order.save()

        #    cart = request.session.get('cart', {})
            #total = 0
            #for id, quantity in cart.items():
            #    product = get_object_or_404(Product, pk=id)
            #    total += quantity * product.price
            #    order_line_item = OrderLineItem(
            #        order = order,
            #        product = product,
            #        quantity = quantity
            #        )
            #    order_line_item.save()

        #messages.error(request, "You have successfully paid")
        #request.session['cart'] = {}
    #else:
        #order_form = OrderForm()

    #return redirect(reverse('index'))
    #return render(request, "checkout.html", {'order_form': order_form})
