from django.shortcuts import render
import mysql.connector as sql
def homepageaction(request):
    return render(request,'welcome.html')