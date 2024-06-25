from django import forms
from courses.models import Courses

class CoursesForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ["title","imgURL","content","isActive","category"]
        widgets = {
            "title": forms.TextInput(attrs={"class":"form-control mb-1"}),
            # "imgURL": forms.TextInput(attrs={"class":"form-control mb-1"}),
            "imgURL": forms.FileInput(attrs={"class":"form-control mb-1"}),
            "content": forms.TextInput(attrs={"class":"form-control mb-1"}),
            "isActive": forms.CheckboxInput(attrs={"class":"form-check mb-1"}),
            "category": forms.SelectMultiple(attrs={"class":"form-control mb-3"}),
        }
        # error_messages = {
        # }