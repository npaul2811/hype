from django.db import models

# Create your models here.
class Tag(models.Model):
    slug = models.SlugField(max_length=255, blank=True)

    def __str__(self):
        return self.slug


class Post(models.Model):
    """ Model for post """
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    body = models.TextField()
    published_on = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    slug  = models.SlugField(max_length=255, blank=True)
    tag = models.ManyToManyField(Tag, related_name="post")
    edited_on = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.slug



