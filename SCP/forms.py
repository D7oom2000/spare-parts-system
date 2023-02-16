from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from User.models import Customer, Store, Workshop
from .models import Parts, Part_Image, DabrhaRequest, dabrha_offers

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['email', 'username', 'password1', 'password2']




class StoreCreationForm(UserCreationForm):
    class Meta:
        model = Store
        fields = ['email', 'username', 'password1', 'password2']




class WorkshopUserCreationForm(UserCreationForm):
    class Meta:
        model = Workshop 
        fields = ['email', 'username', 'password1', 'password2']

class WorkshopLogin(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))




class AddPartsForm(ModelForm):
    class Meta:
        model = Parts
        fields = '__all__'



class PartsImages(forms.Form):

    image_field = forms.ImageField()



class AddserviceForm(forms.Form):
    name = forms.CharField()
    price = forms.FloatField()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class DabrhaRequestForm(ModelForm):
    class Meta:
        model = DabrhaRequest
        fields = [
        'customer',
        'part_no', 
        'P_name', 
        'car_manu', 
        'car_name', 
        'manufacture_year',
        'original',
        'desc',
        'img'
        ]

class DabrhaRequestFormForStores(ModelForm):
    class Meta:
        model= dabrha_offers
        fields = '__all__'


 