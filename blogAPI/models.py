from django.db import models

from authAPI.models import User
from utilsAPI.models import Category, Tag


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=500, null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=False)
    featured = models.BooleanField(default=False)
    featured_image = models.ImageField(blank=True, null=True, upload_to='uploads/blog/images/')
    image_link = models.URLField(null=True, blank=True)
    excerpt = models.TextField(null=True, blank=True)
    slug = models.SlugField(blank=True, null=True, unique=True)
    date_posted = models.DateTimeField(auto_now=True)
    modified_date = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    likes = models.ManyToManyField('Like', blank=True, related_name='post_likes')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=False)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post.title

