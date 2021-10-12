from django.conf.urls import url
from django.urls import path, include
from django.views.generic import TemplateView

from .views import (post_detail, category_detail,
                    IndexView, AllPostView, PostCreateView, AllCategoryView, PostDelete, EditView)

app_name = 'core'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    path('posts/<int:post_id>/', post_detail, name='post_detail'),
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
    path('posts/all_posts/', AllPostView.as_view(), name='all_posts'),
    path('posts/<int:post_id>/delete/', PostDelete.as_view(), name='post_delete'),
    path('posts/<int:post_id>/delete-success/',
         TemplateView.as_view(template_name='core/delete_success.html'), name='post_delete_success'),
    path('posts/<int:post_id>/edit/', EditView.as_view(), name='post_edit'),
    path('category/', AllCategoryView.as_view(), name='category_all'),
    path('category/<int:category_id>/', category_detail, name='category_detail'),
]
