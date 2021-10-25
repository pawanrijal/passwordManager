from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def index(request):
    return HttpResponse("auth")

from django.core.checks import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.urls import reverse
from .models import passwordUser
from django.contrib.auth.decorators import login_required 
# Create your views here.
def user_login(request):
    if request.method=="GET":
        return render(request,"login.html")
        
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('home',user.username)
        else:
            # messages.error(request,'Password donot match')
            return redirect('login')
    
    



def signup(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        cpassword=request.POST.get("cpassword")
        if password==cpassword:
            if len(password)>=8 and len(cpassword)>=8:
                print("password matched")
                if User.objects.filter(username=username).exists():
                    messages.Error(request,"Username or password is invalid")
                    
                    return redirect('signup')
                else:
                    
                    user=User.objects.create_user(username=username,password=cpassword)
                    passwordUser.objects.create(user=user)
                    return redirect('login')
            else:
                
                print("password donot match")
                messages.Error(request,"Password must be atleast 8 characters")
                return redirect('signup')

        else:
            messages.Error(request,"Password donot match")
            return redirect('signup')

    return render(request,"signup.html")


# @login_required
# def logout_view(request):
#     logout(request)
#     return redirect("login")