from django.db import models
from django.utils.text import slugify

# Create your models here.
    
class Categories(models.Model):
    title = models.CharField(max_length=50)
    URL = models.CharField(max_length=50)
    slug = models.SlugField(default="", max_length=50, null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"

class Courses(models.Model):
    title = models.CharField(max_length=50)
    URL = models.CharField(max_length=50)
    imgURL = models.FileField(upload_to="images/", null=True, blank=True)
    content = models.TextField()
    isActive = models.BooleanField()
    # category = models.ForeignKey(Categories, default=1, on_delete=models.CASCADE, related_name="courses",)
    category = models.ManyToManyField(Categories)
    slug = models.SlugField(default="", max_length=50, null=False)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"