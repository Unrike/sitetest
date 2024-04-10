from django.urls import path

from . import views

app_name = "myapp"
urlpatterns = [
    path('', views.home, name='home'),
    path('show/', views.show, name = "show"),
    path('form/', views.index, name = "form"),
    path('accounts/login/', views.user_login, name = 'user_login'),
    path('accounts/logout/', views.user_logout, name = 'user_logout'),
]