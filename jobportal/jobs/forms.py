from dataclasses import field, fields
import imp
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
    


class CustomForm(UserCreationForm) :
    class  Meta:
        model = User
        fields = ('username','password1','password2','email','first_name','last_name')


