from django.contrib import admin
from django.urls import path
from login.views import loginaction
from . import views


urlpatterns = [ path('', views.loginaction,name="login")]