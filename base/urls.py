from django.urls import path
from .views import (home, about, doctor, department, pricing, blog, contact, blog_list)

urlpatterns = [

    path('', home, name='home'),
    path('about/', about, name='about'),
    path('doctor/', doctor, name='doctor'),
    path('department/', department, name='department'),
    path('pricing/', pricing, name='pricing'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('blog-list/', blog_list, name = 'blog-list')

]