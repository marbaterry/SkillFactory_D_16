from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from froala_editor.fields import FroalaField


# class Users(models.Model):
#     pass


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Response(models.Model):
    responseUser = models.ForeignKey(User, on_delete=models.CASCADE)
    responseContent = models.TextField(blank=True)
    responseDate = models.DateTimeField(auto_now_add=True)
    ResponseAllow = models.BooleanField(default=False)

    def __str__(self):
        return self.responseContent


class Post(models.Model):
    postCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    postUser = models.ForeignKey(User, on_delete=models.CASCADE)
    postTitle = models.CharField(max_length=128)
    postContent = models.TextField(blank=True)
    postDate = models.DateTimeField(auto_now_add=True)
    postResponse = models.ManyToManyField(Response, through='CreateResponse')
    content = FroalaField(blank=True)

    def __str__(self):
        return self.postTitle

    def get_absolute_url(self):
        return f'/post/{self.pk}/'


class CreateResponse(models.Model):
    crResponse = models.ForeignKey(Response, on_delete=models.CASCADE)
    crPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    crDate = models.DateTimeField(auto_now_add=True)
    crAllow = models.BooleanField(default=False)


class Comment(models.Model):
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    commentText = models.TextField(blank=True)
    commentDate = models.DateTimeField(auto_now_add=True)
    commentAllow = models.BooleanField(default=False)
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE, default=False)




