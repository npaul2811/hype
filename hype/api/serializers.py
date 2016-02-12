from rest_framework import serializers
from django.contrib.auth.models import User

from blog.models import Post, Tag


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'username'
        ]


class TagSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tag
        fields = [
            'name',
            'slug',
        ]


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer()
    tag = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = [
            'title',
            'slug',
            'author',
            'body',
            'last_edited',
            'published_on',
            'published',
            'tag'
        ]
