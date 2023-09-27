from django.core.mail import send_mail

from django.shortcuts import render,HttpResponse

from django.contrib.auth.models import User

# from ..myApp .form import ContactForm



def login(request):
    # send_mail(
    # "Test Mail",
    # "Hello World",
    # "lecturer2.wadp.nsda@dipti.com.bd",
    # ["rajeshcpi1212@gmail.com"],
    # fail_silently=False,
    # )
    # return HttpResponse("Hello Worlds")
    
    # form= ContactForm()
    # return render(request,"index.html",{
    #     "form" : form
    # })
    return render(request,"login.html")

def signup(request):
    
    if request.method=="POST":
        uname=request.POST.get("username")
        email=request.POST.get("email")
        pass1=request.POST.get("password1")
        pass2=request.POST.get("password2")
        if pass1!=pass2:
            return HttpResponse("Not Match")
        else:
            myuser=User.objects.create_user(uname,email,pass1)
            myuser.save()
            return redirect("login")
    
    return render(request,"signup.html")

def home(request):
    
    return render(request,"home.html")
