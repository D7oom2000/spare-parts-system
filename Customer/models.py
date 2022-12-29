from django.db import models
from User.models import Customer, Store
from Store.models import Ordered_Part

# Create your models here.

# Customer Models are:
#
# class CustomerProfile(models.Model):
# class Customer_orders(models.Model):


class Customer_Order(models.Model):
    co_id = models.IntegerField(primary_key=True)
    S_id = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='StoreOders')
    C_id = models.ForeignKey(Customer, on_delete=models.CASCADE,related_name='CustomerOders')
    op_id = models.ForeignKey(Ordered_Part, on_delete=models.CASCADE)
    Date = models.DateField()