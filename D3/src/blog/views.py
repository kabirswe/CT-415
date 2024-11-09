from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse

from .models import Post
from .forms import PostForm

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

def listPost(request):
    page_title = 'List Post'
    posts = Post.objects.all()
    paginator = Paginator(posts, 2)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_title': page_title,
        "page_obj": page_obj,
    }
    return render(request, 'blog/listPost.html', context)


def updatePost(request, post_id):
    page_title = 'Update Post'
    message = 'Post updated successfully'
    post = Post.objects.get(id=post_id)
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

def deletePost(request, post_id):
    post = Post.objects.get(id=post_id)
    # if request.method == 'POST':
    #     post.delete()
    post.delete()
    return redirect('listPost')
