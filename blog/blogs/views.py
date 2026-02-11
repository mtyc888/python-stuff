from django.shortcuts import render
from .models import Blog
# Create your views here.

def index(request):
    """load the homepage"""
    return render(request, 'blogs/index.xhtml')

def blogs(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    return render(request, 'blogs/blogs.xhtml', context)