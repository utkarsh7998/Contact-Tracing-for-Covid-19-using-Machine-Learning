from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.contrib.auth import authenticate, get_user_model
from .models import *

class InputDataForm(ModelForm):
    
    class Meta:
        model=MLModelData
        fields=['user','file']