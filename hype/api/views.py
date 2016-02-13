from rest_framework import viewsets

from .serializers import PostSerializer, TagSerializer
from blog.models import Post, Tag


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows blog posts to be retrieved or edited.
    """
    queryset = Post.objects.filter(published=True)
    serializer_class = PostSerializer


class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tags to be retrieved or edited.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

