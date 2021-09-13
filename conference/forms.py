from conference.models import Conference
from django import forms
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class ConferenceForm(ModelForm):
    class Meta:
        model = Conference
        fields = '__all__'
