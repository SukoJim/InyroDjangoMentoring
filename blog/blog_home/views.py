from django.shortcuts import render

# Create your views here.
def blog_home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def postDetail(request):
    return render(request, 'postDetail.html')