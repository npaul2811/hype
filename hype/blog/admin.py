from django.contrib import admin

from . import models


class TagInline(admin.TabularInline):
    model = models.Tag.posts.through


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',),
    }
    exclude = [
        'tag',
    ]
    inlines = [
        TagInline,
    ]


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',),
    }
    exclude = [
        'posts',
    ]
