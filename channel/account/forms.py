from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    email = forms.CharField( required=True, widget=forms.EmailInput())

    username = forms.CharField( required=True, widget=forms.TextInput())
    class Meta:
        model = User
        fields = ('username', 'email')
