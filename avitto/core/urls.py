from django.conf.urls import url
from django.conf.urls import url
from django.urls import path, include
from .views import (post_detail, category_detail,
                    category_all, post_create, IndexView, AllPostView)

app_name = 'core'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    path('posts/<int:post_id>/', post_detail, name='post_detail'),
    path('posts/create/', post_create, name='post_create'),
    path('posts/all_posts/', AllPostView.as_view(), name='all_posts'),
    path('category/', category_all, name='category_all'),
    path('category/<int:category_id>/', category_detail, name='category_detail'),
]
