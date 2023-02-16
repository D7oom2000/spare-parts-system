from django.contrib.auth.backends import ModelBackend
from User.models import Customer, Workshop, Store

class CustomerBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            customer = Customer.objects.get(username=username)
        except Customer.DoesNotExist:
            return None
        if customer.check_password(password):
            return customer

class WorkshopBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            workshop = Workshop.objects.get(username=username)
        except Workshop.DoesNotExist:
            return None
        if workshop.check_password(password):
            return workshop

class StoreBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            store = Store.objects.get(username=username)
        except Store.DoesNotExist:
            return None
        if store.check_password(password):
            return store