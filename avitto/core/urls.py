from django.conf.urls import url
from django.conf.urls import url
from django.urls import path, include
from .views import index,  all_posts, post_detail, category_detail, post_edit

urlpatterns = [
    url(r'^$', index, name='index'),
    path('posts/<int:post_id>/', post_detail, name='post_detail'),
    path('posts/<int:post_id>/edit/', post_edit, name='post_edit'),
    path('posts/all_posts/', all_posts, name='all_posts'),
    path('category/', category_detail, name='category_detail'),
]
