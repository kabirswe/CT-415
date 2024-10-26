from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

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
