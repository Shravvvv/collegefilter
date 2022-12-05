from django.shortcuts import render
import mysql.connector as sql

na=''
em=''
pwd=''
# Create your views here.
def signupaction(request):
    global na,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="Shrau@26",database="project")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="name":
                na=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
                
        c="insert into student Value('{}','{}','{}')".format(na,em,pwd)
        cursor.execute(c)
        m.commit()
    return render(request,'signup_page.html')