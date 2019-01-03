from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signupform/', views.signupform, name='signupform'),
    path('signup/', views.signup, name='signup'),
    path('loginform/', views.loginform, name='loginform'),
    path('login/', views.login, name='login'),
    path('signout/', views.signout, name='signout'),
]