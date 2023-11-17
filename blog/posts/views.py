from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from users.models import *
from .forms import *
# Create your views here.

def blog_home(request):
    # 최신 포스트를 가져옵니다.
    latest_post = Post.objects.latest('created_at')

    # 최신 포스트의 이미지를 불러옵니다. 이미지가 없는 경우 None을 반환합니다.
    latest_post_image = latest_post.image.url if latest_post.image else None

    # 모든 포스트를 최신 글 순으로 가져옵니다.
    all_posts = Post.objects.all().order_by('-created_at')


    return render(request, 'home.html', {'all_posts': all_posts, 'latest_post': latest_post, 'latest_post_image': latest_post_image})

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

    # 게시글을 삭제합니다.
    post.delete()

    # 삭제 후 어떤 페이지로 이동할지를 정의합니다.
    return redirect('home')