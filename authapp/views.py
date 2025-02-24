from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



def index(request):
        return render(request, "base.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
                
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("authapp:login")
        messages.error(request, "Invalid username or password")
        return redirect("authapp:login")
    
    return render(request, "store/login.html")



def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
                
        if password != password2:
            messages.error(request, "The two passwords do not match!")
            return redirect("authapp:register")
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect("authapp:register")
        
        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()
        return redirect("authapp:login")
    return render(request, "store/register.html")


def logout_view(request):
    logout(request)
    return render(request, "store/register.html")

