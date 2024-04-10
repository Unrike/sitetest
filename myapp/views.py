from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpRequest
from .forms import UserForm, LoginForm
from .models import UserModel
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def home(request: HttpRequest):
    next = 'myapp:user_login'
    if request.user.is_authenticated:
        next = 'myapp:show'
    return redirect(
        reverse(next)
    )


def index(request: HttpRequest):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, "myapp/index.html", context)

@login_required(redirect_field_name="")
def show(request):
    user_list =  UserModel.objects.all()
    return render(request, "myapp/show.html", {"user_list": user_list})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                    login(request, user)
                    return render(request, 'myapp/suc_login.html')
            else:#elif cd['username'] in User.objects.all.username:
                form.add_error('username', 'Wrong password')
                #return HttpResponse('Invalid login', status_code=401)
    else:
        form = LoginForm()
    return render(request, 'myapp/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return render(request, 'myapp/logout.html')
