from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from users.models import *
# Create your views here.

def blog_home(request):
    # 모든 포스트를 가져옵니다.
    all_posts = Post.objects.all()

    # 최신 포스트를 가져옵니다.
    latest_post = Post.objects.latest('created_at')

    return render(request, 'home.html', {'all_posts': all_posts, 'latest_post': latest_post})


def postDetail(request):
    return render(request, 'postDetail.html')

from django.shortcuts import render, redirect
from .models import Post
from users.models import Category  # Assuming you have a Category model in the users app

def createPost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        category_name = request.POST.get('category')

        # 카테고리가 이미 존재하는지 확인하고, 없으면 새로 생성합니다.
        category, created = Category.objects.get_or_create(category_name=category_name)

        post = Post.objects.create(
            title=title,
            content=content,
            image=image,
            user=request.user,
            category_name=category
        )
        post.save()

        return redirect('home')

    # GET 요청일 경우 폼을 렌더링합니다.
    return render(request, 'createPost.html', {'categories': Category.objects.all()})

def postDetail(request, post_id):
    # Assuming you have a Post model with an 'id' field
    post = Post.objects.get(id=post_id)
    
    context = {
        'post': post,
    }
    
    return render(request, 'postDetail.html', context)