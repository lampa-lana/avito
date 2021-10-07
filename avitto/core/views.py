from django.db.models.aggregates import Sum
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import ListView
from .models import Post, Category, Profile
from .forms import PostForm

# Create your views here.


class IndexView(ListView):
    model = Post
    template_name = 'core/index.html'
    context_object_name = 'posts'
    categories = Category.objects.all()

    def get_queryset(self):
        return self.model.objects.all().order_by('-date_edit')[:7]


# def index(request):
#     # Post.objects.order_by('-date_edit') сортировка в обратном порядке по даде изменения публикации
#     posts = Post.objects.all().order_by('-date_edit')[:7]
#     categories = Category.objects.all()
#     context = {
#         'posts': posts,
#         'categories': categories,
#         'title': "avitto", }
#     return render(request, template_name='core/index.html', context=context)
    # return HttpResponse('Hello world!')

class AllPostView(IndexView):
    template_name = 'core/all_posts.html'

    def get_queryset(self):
        return self.model.objects.all().order_by('category')


# def all_posts(request):
#     # все посты
#     posts = Post.objects.all().order_by('category')
#     context = {
#         'posts': posts,
#         'title': "Все объявления"}
#     return render(request, template_name='core/all_posts.html', context=context)


def post_detail(request, post_id):
    # детали поста
    post = get_object_or_404(Post, id=post_id)
    context = {
        'post': post,
        'title': ("Подробнее об: {}".format(post.post_name))}
    return render(request, template_name='core/post_detail.html', context=context)


def post_create(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'core/post_create.html', {
            'form': form})
    elif request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(reverse('core:post_detail', kwargs={'post_id': post.id}))
        else:
            return render(request, 'core/post_create.html', {
                'form': form})
        # return HttpResponse('post_create')


def category_detail(request, category_id):
    posts = Post.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        'posts': posts,
        'categories': categories,
        'category': category,
        'title': "Побробнее о категориях", }
    return render(request, template_name='core/cat_detail.html', context=context)


def category_all(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'title': "Категории", }
    return render(request, template_name='core/categories.html', context=context)
