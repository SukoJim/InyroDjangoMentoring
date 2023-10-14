from django.shortcuts import render
from .models import UserProfile

# Create your views here.
def blog_home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def postDetail(request):
    return render(request, 'postDetail.html')

