"""Flipcart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

from usermgmt.views import home_view, product_detail_view, product_create_view
from usermgmt.views import registration_view, login_view, customer_login_view, logout_view
from cart.views import view_cart, add_to_cart, adjust_cart, checkout, thankyou


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('login/admin/', admin.site.urls, name='admin'),
    path('', home_view, name='home'),
    path('home/', home_view, name='home'),
    path('register/', registration_view, name="register"),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
    path('customer_login/', customer_login_view, name="customer_login_view"),
    path('create/', product_create_view, name="create"),
    path('product_details/', product_detail_view, name="product_details"),
    path('view_cart/', view_cart, name='view_cart'),
    url(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    url(r'^adjust/(?P<id>\d+)', adjust_cart, name='adjust_cart'),
    path('checkout/', checkout, name="checkout"),
    path('thankyou/', thankyou, name='thankyou')
]
