from django.db import models

class Tag(models.Model):
    slug = models.SlugField(max_length=255, blank=True)

    def __str__(self):
        return self.slug

class Post(models.Model):
    """ Model for post """
    title = models.CharField(max_length=255)
    author = models.ForeignKey('auth.User')
    body = models.TextField()
    edited_on = models.DateTimeField(auto_now=True)
    published_on = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    slug  = models.SlugField(max_length=255, blank=True)
    tag = models.ManyToManyField(Tag, related_name="posts")

    def __str__(self):
        return self.slug



