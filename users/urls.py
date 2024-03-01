from django.contrib import admin
from django.urls import path
from .views import register, logins, landing

urlpatterns = [
    path('register/', register, name=register),
    path('login/', logins, name=logins),
    path('landing/', landing, name=landing)
]
