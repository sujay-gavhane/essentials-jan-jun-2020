from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models import Q


class BlogsQuerySet(models.QuerySet):
    def published(self):
        return self.filter(
            Q(is_published=True)
        )

    def unpublished(self):
        return self.filter(
            Q(is_published=False)
        )


class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    creator = models.ForeignKey(User, related_name='creator', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(default="")
    is_published = models.BooleanField(default=False)
    image = models.ImageField(null=False, blank=False, upload_to="static/images/", default='/static/images/default_blog_image.png')

    def __str__(self):
        return "{0}".format(self.title)

    objects = BlogsQuerySet.as_manager()
