from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from .models import Post, Tag


class BlogIndex(View):

    def get(self, request):
        posts = Post.objects.filter(published=True)
        context = {
            'posts': posts,
        }
        return render(
            request,
            'blog/blog_index.html',
            context,
        )


class BlogSingle(View):

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        context = {
            'post': post,
        }
        return render(
            request,
            'blog/blog_single.html',
            context,
        )