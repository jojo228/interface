from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path("", views.home , name="home"),
    path("404", views.errorpage, name="errorpage"),
    path("project", views.project , name="project"),
    path("service", views.service , name="service"),
    path("about", views.about , name="about"),
    path("contacts", views.contacts , name="contact"),
    path("team", views.team , name="team"),
    path("testimonial", views.testimonial , name="testimonial"),
    path("blog-single", views.blogsingle , name="blog-single"),
    path("blog", views.blog , name="blog"),

    ###### VISA #####
    path("visa_list", views.visa_list , name="visa_list"),
    path("tourist_visa", views.tourist_visa , name="tourist_visa"),

   
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)