from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Create your views here.
def blog_home(request):
    return render(request, 'home.html')

def postDetail(request):
    return render(request, 'postDetail.html')