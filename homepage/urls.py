from django.contrib import admin
from django.urls import path,include  
from homepage.views import homepageaction
from . import views


urlpatterns = [ path('', views.homepageaction,name="homepage")]
