from django import forms
# from localflavor.us.forms import USPhoneNumberField

from .models import Order
from django.contrib.auth.models import User


class OrderForm(forms.ModelForm):
    course = forms.CheckboxSelectMultiple()
    customer_name = forms.CharField(max_length=30,  widget=forms.TextInput(
        attrs={'placeholder': 'Your Name'}))
    telephone = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Telephone'}))
    email = forms.EmailField(max_length=254, required=False, widget=forms.EmailInput(
        attrs={'placeholder': 'Email(optional)'}))

    class Meta:
        model = Order
        fields = ('course', 'customer_name', 'telephone', 'email')


class OrderForm2(forms.ModelForm):
    course = forms.CheckboxSelectMultiple()
    customer_name = User.first_name
    telephone = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Telephone'}))
    email = forms.EmailField(max_length=254, required=False, widget=forms.EmailInput(
        attrs={'placeholder': 'Email(optional)'}))

    class Meta:
        model = Order
        fields = ('course', 'telephone', 'email')

