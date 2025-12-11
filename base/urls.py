from django.urls import path
from .views import (home, about, doctor, department, pricing, Blog, contact, BlogDetailView)

urlpatterns = [

    path('', home, name='home'),
    path('about/', about, name='about'),
    path('doctor/', doctor, name='doctor'),
    path('department/', department, name='department'),
    path('pricing/', pricing, name='pricing'),
    path('blog/', Blog.as_view(), name='blog'),
    path('contact/', contact, name='contact'),
    path('blog-list/<slug:slug>', BlogDetailView.as_view(), name = 'blog-list')

]