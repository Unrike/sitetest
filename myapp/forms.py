from django import forms
from .models import UserModel
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=200, label="First name", widget=forms.TextInput())
    second_name = forms.CharField(max_length=200, label="Last name", widget=forms.TextInput())
    age = forms.IntegerField(label = "Age", widget=forms.TextInput())
    class Meta:
        model = UserModel
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'placeholder': 'Gktaasd fadsf'}))
    password = forms.CharField(widget=forms.PasswordInput, label='Passsword')
