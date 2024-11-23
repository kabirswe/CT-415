from django.contrib import admin

# Register your models here.
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at', 'updated_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'body')
    list_per_page = 25
    list_filter = ('created_at', 'updated_at')
