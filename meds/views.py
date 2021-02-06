from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import meds
import requests
def index(req):
    return render(req, 'meds/index.html')
def signup(req):
    if req.method=='POST':
        username=req.POST['username']
        email=req.POST['email']
        pass1=req.POST['passs']
        pass2=req.POST['repasss']
        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(req, 'Username already exists!!!')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(req, 'Email already exists!!!')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username, password=pass1, email=email)
                user.save()
                return redirect('login')
        else:
            messages.info(req, 'Password does not match')
            return redirect('signup')

        return redirect('/')
    else:
        return render(req, 'meds/signup.html')
    
def login(req):
    if req.method== 'POST':
        user = req.POST['user']
        password = req.POST['password']
        user = auth.authenticate(username=user,password=password)
        if user is not None:
            auth.login(req,user)
            return redirect("/")
        else:
            messages.info(req,'User not found!!!')
            return redirect('login')
    else:
        return render(req, 'meds/login.html')
def logout(req):
    auth.logout(req)
    return redirect('/')
def about(req):
    return render(req, 'meds/about.html')
def appointment(req):
    return render(req, 'meds/appointment.html')
def doctor(req):
    return render(req, 'meds/doctor.html')
def contact(req):
    if req.method== 'POST':
        name=req.POST['name']
        email=req.POST['email']
        text=req.POST['sub']
        user=meds(name=name,email=email,text=text)
        user.save()
    return render(req, 'meds/contact.html')
def faq(req):
    return render(req, 'meds/faq.html')
def department(req):
    return render(req, 'meds/department.html')