from django.shortcuts import render

# Create your views here.
from blog.models import Blog


def welcome(request):
    published_blogs = Blog.objects.published()
    unpublished_blogs = Blog.objects.unpublished()
    return render(request, 'blog/welcome.html',
                  { 'published_blogs': published_blogs,
                    'unpublished_blogs': unpublished_blogs})


def detail(request, blog_id):
    blog = Blog.objects.filter(id=blog_id)
    return render(request, 'blog/detail.html',
                  {'blog': blog})
