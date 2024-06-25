from django.contrib import admin
from .models import Courses, Categories

# Register your models here.

@admin.register(Courses)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "isActive", "slug",)
    readonly_fields = ("slug",)
    list_editable = ("isActive",)
    list_filter = ("isActive", "category")
    search_fields = ("title", "slug", "category",)



@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    pass