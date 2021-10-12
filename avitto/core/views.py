from django.db.models.aggregates import Sum
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Category, Profile
from .forms import PostForm

# Create your views here.


class IndexView(ListView):
    model = Post
    template_name = 'core/index.html'
    context_object_name = 'posts'

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


class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = 'core/post_create.html'
    login_url = '/admin/login'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(reverse('core:post_detail', kwargs={'post_id': post.id}))
        else:
            return render(request, 'core/post_create.html', {
                'form': form})


# def post_create(request):
#     if request.method == 'GET':
#         form = PostForm()
#         return render(request, 'core/post_create.html', {
#             'form': form})
#     elif request.method == "POST":
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             return redirect(reverse('core:post_detail', kwargs={'post_id': post.id}))
#         else:
#             return render(request, 'core/post_create.html', {
#                 'form': form})
        # return HttpResponse('post_create')

class PostDelete(DeleteView):
    model = Post
    pk_url_kwarg = 'post_id'
    template_name = 'core/post_delete.html'

    def get_success_url(self):
        post_id = self.kwargs['post_id']
        return reverse('core:post_delete_success', args=(post_id, ))


class EditView(UpdateView):
    model = Post
    pk_url_kwarg = 'post_id'
    template_name = 'core/post_edit.html'
    form_class = PostForm

    def get_success_url(self):
        post_id = self.kwargs['post_id']
        return reverse('core:post_detail', args=(post_id, ))


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


class AllCategoryView(ListView):
    model = Category
    template_name = 'core/categories.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return self.model.objects.all()


# def category_all(request):
#     categories = Category.objects.all()
#     context = {
#         'categories': categories,
#         'title': "Категории", }
#     return render(request, template_name='core/categories.html', context=context)
