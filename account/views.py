from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def userLogin(request):
    if request.user.is_authenticated:
        return redirect("homepage")
    if request.method=="POST":
        form = LoginForm(request, request.POST)
        print("0")
        if form.is_valid():
            print("1")
            user = authenticate(request, username=form.clean().get('username'), password=form.clean().get('password'))
            if user is not None:
                login(request, user)
                return redirect("homepage")
            else:
                raise ValidationError("Yanlış giriş")
        else:
            raise ValidationError("Yanlış giriş")
    else:
        print("sa")
        form = LoginForm()
    return render(request, "login.html", {
        "form":form
    })

def userLogout(request):
    logout(request)
    return redirect("homepage")

def userRegister(request):
    if request.user.is_authenticated:
        return redirect("homepage")
    if request.method=="POST":
        form = RegisterForm(request.POST)
        print("0")
        if form.is_valid():
            form.save()
            print("1")
            return redirect("homepage")
        else:
            raise ValidationError("Yanlış giriş")
    else:
        print("sa")
        form = RegisterForm()
    return render(request, "register.html", {
        "form":form
    })