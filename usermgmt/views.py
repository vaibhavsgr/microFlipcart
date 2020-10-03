import random

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .phone_backend import PhoneBackend
from .forms import ProductForm, RegistrationForm, AccountAuthenticationForm, CustomerAccountAuthenticationForm
from .models import Product
from cart.models import Order


def index(request):
    return render(request, "index.html")


def registration_view(request):
    context = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "home.html")
        else:
            context['registration_form'] = form
            return render(request, 'register.html', context)            
    else:
        form = RegistrationForm()
        context['registration_form'] = form
        return render(request, 'register.html', context)


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("home")

    if request.method == 'POST':
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_superuser or user.is_staff:
                    print (user)
                    login(request, user)
                    return redirect('admin/')
                else:
                    return redirect('customer_login/')
            else:
                messages.error(request, "Invalid username or password.")
                return render(request, 'login.html', context={"form":form})

    form = AccountAuthenticationForm()
    context['login_form'] = form
    return render(request, 'login.html', context)


def customer_login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("home")

    if request.method == 'POST':
        form = CustomerAccountAuthenticationForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data.get('phone')
            otp   = form.cleaned_data.get('otp')
            user = PhoneBackend.authenticate(username=phone, input_OTP=otp, backend='PhoneBackend')
            #print ("Customer login view after authenticate {} {} {} ".format(user, phone, otp))
            if user is not None:
                login(request, user, backend='usermgmt.phone_backend.PhoneBackend')
                return redirect('home/')
            else:
                messages.error(request, "Invalid Phone")

    form = CustomerAccountAuthenticationForm()
    actual_OTP = generate_otp()
    return render(request, "customer_login.html", {"form":form})


def logout_view(request):
    logout(request)
    return render(request, "home.html")


def home_view(request, *args, **kwargs):
    print (request.user)
    allProducts = Product.objects.all()
    return render(request, "home.html", {'Products':allProducts})


@login_required
def past_orders_view(request):
    print (request.user)
    #allOrders = Order.objects.all()
    allOrders = Order.objects.filter(full_name=request.user)
    return render(request, "orders.html", {'Orders':allOrders})

@login_required
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form':form
    }
    return render(request, "product_create.html", context)


def product_detail_view(request):
    print (request.user)
    allProducts = Product.objects.all()
    return render(request, "product_detail.html", {'Products':allProducts})


def generate_otp():
    otp = random.randint(111111,999999)
    print (otp)
    return otp
