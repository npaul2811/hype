from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from .models import Post, Tag


class BlogIndex(View):

    def get(self, request):
        queryset = Post.objects.filter(is_published=True)
        context = {
            'posts': queryset,
        }
        return render(
            request,
            'blog/blog_index.html',
            context,
        )


class BlogSingle(View):

    def get(self, request, slug):
        post = get_object_or_404(slug=slug)
        context = {
            'post': post,
        }
        return render(
            request,
            'blog_single.html',
            context,
        )