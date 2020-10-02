from django.conf.urls import url
from .views import view_cart, add_to_cart, adjust_cart, checkout, thankyou


urlpatters = [
    path('view_cart/', view_cart, name='view_cart'),
    url(r'^$', view_cart, name='view_cart'),
    path(r'add_to_cart/(?P<id>\d+)', add_to_cart, name="add_to_cart"),
    url(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    path('adjust_cart/', adjust_cart, name="adjust_cart"),
    path('checkout/', checkout, name="checkout"),
    path('thankyou/', thankyou, name='thankyou')
]
