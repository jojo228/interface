from django.shortcuts import render

# Create your views here.
def home(request):
    
    return render(request, "index.html")


def errorpage(request):
    
    return render(request, "404.html")


def about(request):
    
    return render(request, "about.html")


def contacts(request):
    
    return render(request, "contact-2.html")


def project(request):
    
    return render(request, "project.html")


def service(request):
    
    return render(request, "services-1.html")


def team(request):
    
    return render(request, "team.html")



def testimonial(request):
    
    return render(request, "testimonial.html")



def blogsingle(request):
    
    return render(request, "blog-single.html")

def blog(request):
    
    return render(request, "blog.html")


######## VISA ########
def visa_list(request):
    
    return render(request, "visa-list.html")

def tourist_visa(request):
    
    return render(request, "tourist-visa.html")


