from django.shortcuts import render,HttpResponseRedirect
from .models import Password,passwordUser
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse




#form

class PasswordForm(forms.ModelForm):

    class Meta:
        model=Password
        fields=["websiteName","password"]
        widgets={
            "websiteName":forms.TextInput(attrs={"class":"form-control"}),
            "password":forms.TextInput(attrs={"class":"form-control"}),
        }




@login_required
def home(request,username):
    Passwords=passwordUser.objects.get(user=User.objects.get(username=username))
    context={
        'passwords':Passwords,
    }
    
    return render(request,"home.html",context)
    



def addPassword(request):
    
    
        form=PasswordForm(request.POST or None)
        if request.method=="POST":
            if form.is_valid():
                form.cleaned_data["passworduser"]=request.user.passworduser
                Password.objects.create(**form.cleaned_data)
                
        context={
            "form":form
            
            }
        return render(request,"addpassword.html",context)
def homepage(request):
    return render(request,"homepage.html")