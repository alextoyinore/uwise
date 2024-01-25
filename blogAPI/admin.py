from django.contrib import admin

from blogAPI.models import Post, Like, Comment


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted', 'is_published')
    search_fields = ('title', 'author', 'date_posted', 'is_published')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'date')
    search_fields = ('post', 'author', 'date')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'content', 'date')
    search_fields = ('post', 'author', 'content', 'date')
