from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from .views import welcome, detail


urlpatterns = [
    url(r'login$', LoginView.as_view(template_name="blog/login_form.html"), name='blogger_login'),
    url(r'logout$', LogoutView.as_view(), name="blogger_logout"),
    url(r'^blog/<int:blog_id>$', detail, name='blog_detail'),
    url(r'^$', welcome, name="welcome")
]
