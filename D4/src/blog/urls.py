from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>/', views.detail, name='detail'),
    path('about/', views.about, name='about'),
    path('post/create/', views.createPost, name='createPost'),
    path('post/list/', views.listPost, name='listPost'),
    path('post/update/<int:post_id>/', views.updatePost, name='updatePost'),
    path('post/delete/<int:post_id>/', views.deletePost, name='deletePost'),

    path('api/posts/', views.getApiPost, name='get_posts'),
]
