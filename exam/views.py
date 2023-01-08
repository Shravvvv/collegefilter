from django.shortcuts import render

# Create your views here.
def subexam(request):
    return render(request,'exam.html')