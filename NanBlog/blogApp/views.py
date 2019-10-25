from django.shortcuts import render

# Create your views here.

def index(request):
    
    return render(request,'pages/index.html')


def category(request):
    
    return render(request,'pages/category.html')

def single_blog(request):
    
    return render(request,'pages/single_blog.html')


def archive(request):
    
    return render(request,'pages/archive.html')

def contact(request):
    
    return render(request,'pages/contact.html')

def login(request):
    
    return render(request,'pages/login.html')

def register(request):
    
    return render(request,'pages/register.html')