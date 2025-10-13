from django.shortcuts import render
from django.views.generic import ListView
from .models import News

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def doctor(request):
    return render(request, 'pages/doctor.html')

def department(request):
    return render(request, 'pages/departament.html')

def pricing(request):
    return render(request, 'pages/pricing.html')

def blog(request):  
    posts = News.objects.all()
    context = {
        'News': posts
    }
    return render(request, 'pages/blog.html', context)

def contact(request):           
    return render(request, 'pages/contact.html')

def blog_list(request):
    return render(request, 'pages/blog-list.html')


class NewsView(ListView):
    model = News
    template_name = 'blog.html'

