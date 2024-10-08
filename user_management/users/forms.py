from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Product

class SignUpForm(UserCreationForm):
    username = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    email = forms.EmailField(label="",widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    password1 = forms.CharField(label="",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    password2 = forms.CharField(label="",widget= forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm password'}))
    
    class Meta:
        model = User
        fields = ('username','email','password1','password2')



