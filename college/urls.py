from django.contrib import admin
from django.urls import path
from college.views import subcollege
from . import views


urlpatterns = [ path('', views.subcollege,name="college")]