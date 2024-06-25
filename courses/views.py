from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from .models import *

# Create your views here.

def course(request, category):
    paginator = Paginator(Courses.objects.filter(URL__contains=f"{category}"), 2)
    return render(request, "course.html", {
        "paginator" : paginator,
        "categories" : Categories.objects.all(),
        "courses" : paginator.get_page(request.GET.get("page", 1)),
        # "course" : Categories.objects.get(slug=f"{course}"),
        "selectedCategory" : f"{category}",
    })

def courses(request):
    return render(request, "courses.html", {
        "categories" : Categories.objects.all(),
        "courses" : Courses.objects.all(),
    })

def notFound(request):
    return render(request, "notfound.html", status=500)