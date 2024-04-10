from django import forms
from .models import UserModel
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'placeholder': 'Gktaasd fadsf'}))
    password = forms.CharField(widget=forms.PasswordInput, label='Passsword')
