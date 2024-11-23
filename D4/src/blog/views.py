from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Post
from .forms import PostForm
from .serializer import PostSerializer

# Create your views here.
def index(request):
    posts = Post.objects.all()
    page_title = 'Blog page'
    home_content = 'our homepage content should be tailored to your specific target audience and brand voice. By following these guidelines, you can create a homepage that captures attention, engages visitors, and drives conversions.'
    context = {
        'posts': posts,
        'page_title': page_title,
        'home_content': home_content
    }
    return render(request, 'blog/index.html', context)

def about(request):
    return HttpResponse("About the blog.")

def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    page_title = 'Post || ' + post.title
    context = {
        'post': post,
        'page_title': page_title
    }
    return render(request, 'blog/detail.html', context)

@login_required
def createPost(request):
    page_title = 'Post create page'
    message = 'Post created successfully'
    form = PostForm
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('listPost')
    context = {
        'form': form,
        'page_title': page_title
    }
    return render(request, 'blog/createPost.html', context)

@login_required
def listPost(request):
    page_title = 'List Post'
    posts = Post.objects.filter(author=request.user)
    paginator = Paginator(posts, 2)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_title': page_title,
        "page_obj": page_obj,
    }
    return render(request, 'blog/listPost.html', context)


@login_required
def updatePost(request, post_id):
    page_title = 'Update Post'
    message = 'Post updated successfully'
    post = Post.objects.get(id=post_id)
    if post.author != request.user:
        return redirect('listPost')
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('listPost')
    context = {
        'form': form,
        'page_title': page_title,
        'message': message
    }
    return render(request, 'blog/createPost.html', context)

@login_required
def deletePost(request, post_id):
    post = Post.objects.get(id=post_id)
    if post.author != request.user:
        return redirect('listPost')
    post.delete()
    return redirect('listPost')

@api_view(['GET'])
def getApiPost(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)