from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Category, Profile

# Create your views here.


def index(request):
    # Post.objects.order_by('-date_edit') сортировка в обратном порядке по даде изменения публикации
    posts = Post.objects.all().order_by('-date_edit')[:7]
    categorys = Category.objects.all()
    context = {
        'posts': posts,
        'categorys': categorys,
        'title': "avitto"}
    return render(request, template_name='core/index.html', context=context)
    # return HttpResponse('Hello world!')


def all_posts(request):
    # все посты
    return HttpResponse('all_posts')


def post_detail(request, post_id):
    # детали поста
    return HttpResponse('post_detail')


def post_edit(request, post_id):
    # изменние  поста
    return HttpResponse('post_edit')


# def category_detail(request):
#     return HttpResponse('category_detail')


def category_detail(request):
    categorys = Category.objects.all()
    context = {
        'categorys': categorys,
        'title': "categorys"}
    return render(request, template_name='core/categorys.html', context=context)
