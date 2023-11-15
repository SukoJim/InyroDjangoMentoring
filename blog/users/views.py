from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 사용자 인증
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # 인증이 성공한 경우, 사용자를 로그인 상태로 만듦
            login(request, user=user)
            # 로그인 이후에 리다이렉트할 URL 설정 (홈 페이지)
            return redirect('home')
        else:
            # 인증에 실패한 경우에 대한 처리
            return render(request, 'login.html', {'error_message': 'Invalid login credentials'})

    # GET 요청에 대한 처리
    return render(request, 'login.html')

def user_logout(request):
    # 인증 성공 사용자에 대한 로그아웃 함수
    logout(request)
    
    # 로그아웃 요청시 로그아웃 후 홈으로 이동
    return redirect('home')


def register(request):

    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method =="POST":
        username = request.POST.get('userID')
        nickname = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        regis = UserProfile.objects.create_user(
            username = username, nickname = nickname, email = email, password = password) 
        regis.save()
        
    return render(request, 'home.html')