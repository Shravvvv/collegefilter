from django.contrib import admin
from django.urls import path,include  
from signup.views import signupaction
from . import views


urlpatterns = [ path('', views.signupaction,name="signup")]