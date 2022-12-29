from django.db import models
from User.models import Store
from time import gmtime, strftime

# Create your models here.

# Store Models are:
#
# class StoreProfile(models.Model):
# class Part(models.Model):
# class Part_Image(models.Model):
# class Store_Part(models.Model):
# class Ordered_Part(models.Model):
# class Store_Image(models.Model):


class Part(models.Model):
    part_no = models.IntegerField(primary_key=True)
    P_name = models.CharField(max_length=100)

   
class Part_Image(models.Model):
    P_id = models.ForeignKey(Part, on_delete=models.CASCADE)
    image_field = models.ImageField(
        upload_to= 'static/images/PartImages/{0}'.format(strftime('%Y%m%d-%H%M%S',gmtime())) ,
        default='no-image.jpg' ,
        width_field='imagewidth' ,
        height_field='imageheight' ,
        )
    imagewidth = models.PositiveIntegerField(editable = False, default = 65)
    imageheight = models.PositiveIntegerField(editable = False, default = 65)


class Store_Part(models.Model):
    sp_id = models.IntegerField(primary_key=True)
    S_id = models.ForeignKey(Store, on_delete=models.CASCADE,  related_name='Storepart')
    part_no = models.ForeignKey(Part, on_delete=models.CASCADE)
    P_name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    car_make = models.CharField(max_length=50)


class Ordered_Part(models.Model):
    op_id = models.IntegerField(primary_key=True)
    sp_id = models.ForeignKey(Store_Part, on_delete=models.CASCADE, related_name='Storepart')


class Store_Image(models.Model):
    S_id = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='StoreInformation')
    image_field = models.ImageField(
        upload_to= 'static/images/StoreProfile/{0}'.format(strftime('%Y%m%d-%H%M%S',gmtime())) ,
        default='no-image.jpg' ,
        width_field='imagewidth' ,
        height_field='imageheight' ,
        )
    imagewidth = models.PositiveIntegerField(editable = False, default = 50)
    imageheight = models.PositiveIntegerField(editable = False, default = 50)


