from django.urls import path
from . import views

urlpatterns =[
    path('', views.courses, name="coursesSlug"),
    path('<category>/', views.course, name="categorySlug"),
    path('<notFound>/', views.notFound),
    # path('programming/', views.programming),
    # path('web-development/', views.webDevelopment),
    # path('mobile-application-development/', views.mobileApplicationDevelopment),
]