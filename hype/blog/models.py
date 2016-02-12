from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Tag(models.Model):
    """
    Base tag model. Can be applied to any other model through a many to many
    relationship.
    """
    name = models.CharField(
        verbose_name='Tag Name',
        blank=False,
        max_length=255,
    )
    slug = models.SlugField(
        verbose_name='Tag Slug',
        blank=True,
        max_length=300,
    )

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Defines basic post model. All blog posts are instances of this model.
    """
    title = models.CharField(
        verbose_name='Title',
        blank=False,
        max_length=255,
    )
    slug = models.SlugField(
        verbose_name='Post Slug',
        blank=True,
        max_length=300,
    )
    author = models.ForeignKey(
        User,
        verbose_name='Author',
        related_name='posts',
        blank=False,
        null=False,
    )
    body = models.TextField(
        verbose_name='Body',
        blank=True,
    )
    last_edited = models.DateTimeField(
        verbose_name='Last Edited',
        auto_now=True,
        blank=False,
        null=False,
    )
    published_on = models.DateTimeField(
        verbose_name='Time Published',
        auto_now=True,
        blank=False,
        null=False,
    )
    published = models.BooleanField(
        verbose_name='Is Published',
        default=False,
    )
    tag = models.ManyToManyField(
        Tag,
        verbose_name='Tag',
        related_name='posts',
        blank=True,
    )

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def is_published(self):
        """
        Checks to see if a 'Post' instance has been published.
        :return:
        True if 'published' is true. False if 'published' is false.
        """
        if self.published:
            return True
        else:
            return False

    def save(self, *args, **kwargs):
        if not  self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
