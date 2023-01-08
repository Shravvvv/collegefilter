from django.contrib import admin
from django.urls import path
from course.views import subcourse
from . import views


urlpatterns = [ path('', views.subcourse,name="course")]