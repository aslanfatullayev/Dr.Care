from django.shortcuts import render
from django.views.generic import ListView, DetailView
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


class Blog(ListView):
    model = News
    template_name = 'pages/blog.html'
    context_object_name = "News"
    


def contact(request):           
    return render(request, 'pages/contact.html')


class BlogDetailView(DetailView):
    model = News
    template_name = 'pages/blog-list.html'
    context_object_name = 'new'

class NewsView(ListView):
    model = News
    template_name = 'blog.html'



