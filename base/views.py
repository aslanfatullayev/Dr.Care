from django.shortcuts import render

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
    return render(request, 'pages/blog.html')

def contact(request):           
    return render(request, 'pages/contact.html')

