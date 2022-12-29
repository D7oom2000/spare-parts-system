from django.db import models
from User.models import Workshop
from Store.models import Ordered_Part
from time import gmtime, strftime


# Create your models here.



# Workshop Models are:
#
# class WorkshopProfile(models.Model):
# class Workshop_orders(models.Model):
# class Workshop_Image(models.Model):
# class Services(models.Model):
# class Appointment(models.Model):
# class Offers(models.Model):


class Workshop_Order(models.Model):
    wo_id = models.IntegerField(primary_key=True)
    W_id = models.ForeignKey(Workshop, on_delete=models.CASCADE, related_name='Workshoporders')
    op_id = models.ForeignKey(Ordered_Part, on_delete=models.CASCADE)


class Workshop_Image(models.Model):
    W_id = models.ForeignKey(Workshop, on_delete=models.CASCADE, related_name='WorkshopImg')
    image_field = models.ImageField(
        upload_to= 'static/images/WorkShopProfile/{0}'.format(strftime('%Y%m%d-%H%M%S',gmtime())) ,
        default='no-image.jpg' ,
        width_field='imagewidth' ,
        height_field='imageheight' ,
        )
    imagewidth = models.PositiveIntegerField(editable = False, default = 50)
    imageheight = models.PositiveIntegerField(editable = False, default = 50)


class Service(models.Model):
    service_id = models.IntegerField(primary_key=True)
    W_id = models.ForeignKey(Workshop, on_delete=models.CASCADE, related_name='WorkshopServices')
    name = models.CharField(max_length=75)


class Appointment(models.Model):
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    W_id = models.ForeignKey(Workshop, on_delete=models.CASCADE, related_name='WorkshopAppointment')
    C_id = models.ForeignKey(Workshop, on_delete=models.CASCADE, related_name='CustomerAppointment')
    Date = models.DateField()
    Time = models.TimeField()


class Offer(models.Model):
    offer_id = models.IntegerField(primary_key=True)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    W_id = models.ForeignKey(Workshop, on_delete=models.CASCADE, related_name='WorkshopOffers')
    offer_desc = models.CharField(max_length=200)
    offer_price = models.IntegerField()