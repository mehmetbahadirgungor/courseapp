from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .forms import CoursesForm
from django.core.paginator import Paginator
from courses.models import *

# Create your views here.

def index(request):
    return render(request, "index.html", {
        "categories" : Categories.objects.all(),
        "courses" : Courses.objects.all(),
    })

def search(request):
    
    if "q" in request.GET and request.GET["q"] != "":
        q = request.GET["q"]
        paginator = Paginator(Courses.objects.filter(title__contains=f"{q}"), 2)
        return render(request, "course.html", {
            "paginator" : paginator,
            "categories" : Categories.objects.all(),
            "courses" : paginator.get_page(request.GET.get("page", 1)),
            # "course" : Categories.objects.get(slug=f"{q}"),
            # "selectedCategory" : f"{q}",
        })
    else:
        return redirect("/courses")

def contact(request):
    return render(request, "contact.html")

def createCourse(request):
    if not request.user.is_superuser:
        return redirect("homepage")
    if request.method == "POST":
        print(request.POST)
        form = CoursesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/courselist")
    else:
        form = CoursesForm()

    return render(request, "createcourse.html", {
        "form" : form
    })

def courseEdit(request, course):
    if not request.user.is_superuser:
        return redirect("homepage")

    obj = get_object_or_404(Courses, slug=course) 
    
    if request.method == "POST":
        print(request.FILES["imgURL"].name)
        request.FILES["imgURL"].name = f"{obj.slug}.jpg"
        form = CoursesForm(request.POST, request.FILES, instance=obj)
        print(request.POST)
        form.save()
        return redirect("courselist")
    else:
        form = CoursesForm(instance=obj)

    return render(request, "course-edit.html", {
        "form" : form,
        "course" : course,
    })

def courselist(request):
    if not request.user.is_superuser:
        return redirect("homepage")
    
    if request.method == "POST":
        print(request.POST)
        # Courses.objects.filter(slug=request.POST["slug"]).delete()

    return render(request, "courselist.html", {
        "courses" : Courses.objects.all(),
    })

def about(request):
    return render(request, "about.html")

def notFound(request, category):
    return render(request, "notfound.html")