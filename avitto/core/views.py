from django.db.models.aggregates import Sum
from django.contrib.auth.decorators import login_required
from django.forms.models import modelform_factory, modelformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.template import Context, loader
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView, View
from .models import Post, Category, Profile
from .forms import PostForm
from django.forms import modelformset_factory

# Create your views here.


class IndexView(ListView):
    model = Post
    template_name = 'core/index.html'
    context_object_name = 'posts'
    extra_context = {'page_title': 'Главная'}

    # def get_queryset(self):
    #     return self.model.objects.all().order_by('-date_edit')[:7]

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['posts'] = self.model.objects.all().order_by(
            '-date_edit').filter(draft=False).order_by('-date_edit')[:7]
        context['category'] = Category.objects.all()
        return context


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
    extra_context = {'page_title': 'Все объявления'}

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['posts'] = self.model.objects.all().order_by(
            '-date_edit').filter(draft=False)
        context['category'] = Category.objects.all()
        return context


# def all_posts(request):
#     # все посты
#     posts = Post.objects.all().order_by('category')
#     context = {
#         'posts': posts,
#         'title': "Все объявления"}
#     return render(request, template_name='core/all_posts.html', context=context)

class PostDetailView(DetailView):
    model = Post
    pk_url_kwarg = "post_id"
    template_name = 'core/post_detail.html'
    extra_context = {'page_title': 'Подробнее об объявлении'}

    def get(self, request, post_id, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['posts'] = Post.objects.filter(draft=True)
        context['categories'] = Category.objects.all()

        return self.render_to_response(context)


# def post_detail(request, post_id):
#     # детали поста
#     post = get_object_or_404(Post, id=post_id)
#     context = {
#         'post': post,
#         'title': ("Подробнее об: {}".format(post.post_name))}
#     return render(request, template_name='core/post_detail.html', context=context)


class PostCreateView(CreateView):
    form_class = PostForm
    template_name = 'core/post_create.html'
    login_url = '/admin/login'
    extra_context = {'page_title': 'Создать объявление'}

    @method_decorator(login_required)
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
    extra_context = {'page_title': 'Удалить объявление'}

    def get_success_url(self):
        post_id = self.kwargs['post_id']
        return reverse('core:post_delete_success', args=(post_id, ))


class EditView(UpdateView):
    model = Post
    pk_url_kwarg = 'post_id'
    template_name = 'core/post_edit.html'
    form_class = PostForm
    extra_context = {'page_title': 'Изменить объявление'}

    def get_success_url(self):
        post_id = self.kwargs['post_id', ]
        return reverse('core:post_detail', args=(post_id, ))


class CategoriesDetailView(DetailView):
    model = Category
    pk_url_kwarg = "category_id"
    template_name = 'core/cat_detail.html'
    extra_context = {'page_title': 'Об категории'}

    def get(self, request, category_id, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['posts'] = Post.objects.filter(category_id=category_id)
        context['category'] = Category.objects.get(pk=category_id)
        context['categories'] = Category.objects.all()

        return self.render_to_response(context)


# def category_detail(request, category_id):
#     posts = Post.objects.filter(category_id=category_id)
#     categories = Category.objects.all()
#     category = Category.objects.get(pk=category_id)
#     context = {
#         'posts': posts,
#         'categories': categories,
#         'category': category,
#         'title': "Побробнее о категориях", }
#     return render(request, template_name='core/cat_detail.html', context=context)


class AllCategoryView(ListView):
    model = Category
    template_name = 'core/categories.html'
    context_object_name = 'categories'
    extra_context = {'page_title': 'Категории'}

    def get_queryset(self):
        return self.model.objects.all()


# def category_all(request):
#     categories = Category.objects.all()
#     context = {
#         'categories': categories,
#         'title': "Категории", }
#     return render(request, template_name='core/categories.html', context=context)


# def pageNotFound(request, exception):
#     return HttpResponseNotFound('<h1> Страница не найдена</h1>')
#
# class PostCreateView(CreateView):
#     form_class = PostForm
#     template_name = 'core/post_create.html'
#     login_url = '/admin/login'
#     extra_context = {'page_title': 'Создать объявление'}
#     ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=3)

#     @method_decorator(login_required)
#     def add_pet_view(self, request, *args, **kwargs):
#         if request.method == "GET":
#             self.object = self.get_object()
#             form = PostForm
#             formset = self.ImageFormSet(queryset=Image.objects.none())
#             return render(self.request, self.template_name, {'form': form, 'formset': formset})
#         elif request.method == "POST":
#             form = PostForm(request.POST)
#             formset = self.ImageFormSet(
#                 request.POST, request.FILES, queryset=Image.objects.none())
#             if form.is_valid() and formset.is_valid():
#                 post = form.save(commit=False)
#                 post.author = request.user
#                 post.save()
#                 for form in formset.cleaned_data:
#                     image = form['image']
#                     photo = Image(post=post, image=image)
#                     photo.save()
#                 return redirect(reverse('core:post_detail', kwargs={'post_id': post.id}))
#         else:
#             form = PostForm
#             formset = self.ImageFormSet(queryset=Image.objects.none())
#             return render(request, self.template_name, {
#                 'form': form, 'formset': formset}, context_instance=self.RequestContext(request))


# def add_pet_view(request):
#     ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=3)
#     if request.method == "GET":
#         form = PostForm
#         formset = ImageFormSet(queryset=Image.objects.none())
#         return render(request, 'core/post_create.html', {'form': form, "formset": formset})
#     elif request.method == "POST":
#         form = PostForm(request.POST, request.FILES)
#         formset = ImageFormSet(request.POST, request.FILES)
#     if form.is_valid() and formset.is_valid():
#         post = form.save(commit=False)
#         post.author = request.user
#         post.save()
#         for form in formset.cleaned_data:
#             if form:
#                 image = form['image']
#                 photo = Image(post=post, image=image)
#                 photo.save()
#         return redirect(reverse('core:post_detail', kwargs={'post_id': post.id}))
#     else:
#         return render(request, 'core/post_create.html', {
#             'form': form, "formset": formset})
