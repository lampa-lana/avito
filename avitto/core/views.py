from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.


def index(request):
    # Post.objects.order_by('-date_edit') сортировка в обратном порядке по даде изменения публикации
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'title': "Список обьявлений"}
    return render(request, template_name='posts/index.html', context=context)
    # return HttpResponse('Hello world!')


def index2(request):
    return HttpResponse('Hello People!')
