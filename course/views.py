from django.shortcuts import render

# Create your views here.
def subcourse(request):
    return render(request,'course.html')