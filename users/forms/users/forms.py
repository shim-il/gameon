from django.contrib.auth import forms
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

#from users.models import Order


'''
class OrderForms(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
'''

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



