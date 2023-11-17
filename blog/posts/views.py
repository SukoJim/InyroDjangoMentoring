from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from users.models import *
from .forms import *
import os
from django.conf import settings
from datetime import datetime

# Create your views here.

def blog_home(request):
    # 최신 포스트를 가져옵니다.
    latest_post = Post.objects.latest('created_at')

    # 최신 포스트의 이미지를 불러옵니다. 이미지가 없는 경우 None을 반환합니다.
    latest_post_image = latest_post.image.url if latest_post.image else None

    # 모든 포스트를 최신 글 순으로 가져옵니다.
    all_posts = Post.objects.exclude(id=latest_post.id).order_by('-created_at')


    return render(request, 'home.html', {'all_posts': all_posts, 'latest_post': latest_post, 'latest_post_image': latest_post_image})

### Post CRUD ###
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
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post).select_related('user')  # 댓글과 작성자 정보를 함께 가져오기
    return render(request, 'postDetail.html', {'post': post, 'comments': comments})

def editPost(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        print(form)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('postDetail', post_id=post.id)
        else:
            print(form.errors)  # Print form errors to the console for debugging
    else:
        form = PostForm(instance=post)

    return render(request, 'editPost.html', {'form': form, 'post': post})


def deletePost(request, post_id):
    # 게시글을 가져오거나 404 에러를 발생시킵니다.
    post = get_object_or_404(Post, id=post_id)

    # 게시글에 연결된 이미지를 가져옵니다.
    post_image = post.image

    # 게시글을 삭제합니다.
    post.delete()

    # 이미지가 존재하면 삭제합니다.
    if post_image:
        # 이미지 파일의 실제 경로를 가져옵니다.
        image_path = os.path.join(settings.MEDIA_ROOT, str(post_image))
        
        # 이미지 파일을 삭제합니다.
        if os.path.exists(image_path):
            os.remove(image_path)

    # 삭제 후 어떤 페이지로 이동할지를 정의합니다.
    return redirect('home')
#######

def add_comment(request, post_id):
    if request.method == 'POST':
        content = request.POST.get('comment')
        user = request.user

        # 댓글을 생성합니다.
        comment = Comment.objects.create(
            content=content,
            user=user,
            created_at=datetime.now(),
            post_id=post_id,  # Link the comment to the post
        )

        return redirect('postDetail', post_id=post_id)

    return redirect('home')