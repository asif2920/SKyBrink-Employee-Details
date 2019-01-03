from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('insertform/', views.insertform, name='insertform'),
    path('insert/', views.insert, name='insert'),
    path('getall/', views.getall, name='getall'),
    path('updateform/', views.updateform, name='updateform'),
    path('updatecheck/', views.updatecheck, name='updatecheck'),
    path('update/', views.update, name='update'),
    path('deleteform/', views.deleteform, name='deleteform'),
    path('deletecheck/', views.deletecheck, name='deletecheck'),
    path('delete/', views.delete, name='delete'),
]