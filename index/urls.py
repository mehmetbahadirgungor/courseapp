from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('', include('account.urls')),
    path('search/', views.search, name="search"),
    path('courses/', include('courses.urls'), name="coursesSlug"),
    path('contact/', views.contact, name="contact"),
    path('createcourse/', views.createCourse, name="createCourse"),
    path('course-edit/<course>', views.courseEdit, name="course-edit"),
    path('courselist/', views.courselist, name="courselist"),
    path('about/', views.about, name="about"),
    path('<category>/', views.notFound),
]