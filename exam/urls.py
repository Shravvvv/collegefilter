from django.contrib import admin
from django.urls import path
from exam.views import subexam
from . import views


urlpatterns = [ path('', views.subexam,name="exam")]