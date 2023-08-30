from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    blog = blogs.objects.filter(show = 1)
    cat = Categories.objects.all()
    context = {'blog': blog, 'cat': cat}
    return render(request, 'home.html', context)

def write(request):
    if request.method == 'POST':
        author = request.POST['author']
        title = request.POST['title']
        content = request.POST['content']
        cat_id = request.POST['cat']
        category = Categories.objects.get(id=cat_id)
        new_blog = blogs(author_name=author, title=title, content=content, catagory=category)
        new_blog.save()
    cat = Categories.objects.all()
    return render(request, 'write.html', {'cat':cat})

def blog_read(request):
    
    blog = blogs.objects.all()
    cat = Categories.objects.all()
    context = {'blog': blog, 'cat': cat}
    return render(request, 'blogs.html', context)

def about(request):
    return render(request, 'about.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def view_specific(request, id):
    blog = blogs.objects.filter(catagory_id=id)
    cat = Categories.objects.all()
    head = Categories.objects.get(id=id)
    return render(request, 'specific.html', {'blog': blog, 'cat': cat, 'head': head})

def read_specific(request, id):
    blog = blogs.objects.filter(id=id)
    blogss = blogs.objects.exclude(id=id)
    cat = Categories.objects.all()
    return render(request, 'read.html', {'blog': blog, 'blogss': blogss, 'cat': cat})