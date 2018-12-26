from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={'placeholder': 'Real Name'}))
    email = forms.EmailField(max_length=254, required=False,  widget=forms.EmailInput(
        attrs={'placeholder': 'Email(optional)'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password1', 'password2', )


