from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from .forms import ProductForm, RegistrationForm, AccountAuthenticationForm, CustomerAccountAuthenticationForm
from .models import Product


# Create your views here.
def index(request):
    return render(request, "index.html")


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            phone = form.cleaned_data.get('phone')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(username=username, password=raw_password)
            if account:
                login(request, account)
                return redirect(request, 'home.html', {})
        else:
            context['registration_form'] = form

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
                login(request, user)
                if user.is_superuser or user.is_staff:
                    return redirect('admin/')
                else:
                    #return render(request, "home.html")
                    return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
                return render(request, 'login.html', context={"form":form})

    form = AccountAuthenticationForm()
    context['login_form'] = form
    return render(request, 'login.html', context)


def customer_login_view(request):
    if request.method == 'POST':
        form = CustomerAccountAuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            #username = form.cleaned_data.get('username')
            phone = form.cleaned_data.get('phone')
            otp = form.cleaned_data.get('otp')
            user = authenticate(phone=phone, otp=otp)
            if user is not None:
                login(request, user)
                return render(request, "home.html")

    form = CustomerAccountAuthenticationForm()
    return render(request = request,
                    template_name = "login.html",
                    context={"form":form})


def logout_view(request):
    logout(request)
    return render(request, "home.html")
    #return HttpResponseRedirect(reverse('home_view'))


def home_view(request, *args, **kwargs):
    print (request.user)
    #return HttpResponse("<H1> Hello World, to the landing page of DeHaat</H1>")
    allProducts = Product.objects.all()
    return render(request, "home.html", {'Products':allProducts})
    #return render(request, "home.html", {})


@login_required
def view_orders(request):
    print (request.user)
    allOrders = Orders.objects.all()
    return


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
    #obj = Product.objects.get(id=1)
    print (request.user)
    allProducts = Product.objects.all()
    return render(request, "product_detail.html", {'Products':allProducts})
