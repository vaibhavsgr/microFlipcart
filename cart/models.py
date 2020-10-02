from django.db import models
from usermgmt.models import Product
# Create your models here.


class Order(models.Model):
    order_id     = models.AutoField(primary_key=True)
    items_json   = models.CharField(max_length=5000)
    full_name    = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    town_or_city = models.CharField(max_length=40, blank=False)
    status       = models.CharField(max_length=15, blank=False)

    def __str__(self):
        return "{0}-{1}-{2}-{3}".format(self.order_id, self.items_json, self.full_name, self.phone_number)



#class OrderLineItem(models.Model):
    #order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    #product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    #quantity = models.IntegerField(blank=False)

    #def __str__(self):
    #    return "{0} {1} @ {2}".format(self.quantity, self.product.name, self.product.price)
