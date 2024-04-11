from django import forms
from .models import UserModel
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=200, label="Имя", widget=forms.TextInput())
    second_name = forms.CharField(max_length=200, label="Фамилия", widget=forms.TextInput())
    age = forms.IntegerField(label = "Возраст", widget=forms.TextInput())
    class Meta:
        model = UserModel
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'placeholder': 'Gktaasd fadsf'}))
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
