from django import forms
from django.contrib.auth import authenticate,  login, logout
from django.contrib.auth.views import LoginView
from django.db import models
from django.forms import fields
from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls.base import reverse
from django.views.generic.edit import DeleteView
from django.views.generic import UpdateView
from django.views.generic.list import ListView
from .forms_auth import LoginForm
from .models import Profile
from .forms_auth import UpdateProfileForm


class MyLoginView(LoginView):
    template_name = 'my_auth/login.html'
    form = LoginForm
    extra_context = {'page_title': 'Личный кабинет'}

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect(reverse('core:index'), request)
            else:
                return render(request, self.template_name, {'form': form})
        else:
            return render(request, self.template_name, {'form': form})


def logout_view(request):
    logout(request)
    return redirect(reverse('core:login'), request)


class ProfileView(DeleteView):
    model = Profile
    template_name = 'my_auth/profile.html'
    extra_context = {'page_title': 'Профиль'}

    def get_object(self):
        return get_object_or_404(self.model, user_id=self.kwargs['user_id'])


class AllProfileView(ListView):
    model = Profile
    template_name = 'my_auth/all_profile.html'
    context_object_name = 'all_profile'
    extra_context = {'page_title': 'Профили пользователей'}

    def get_queryset(self):
        return self.model.objects.all()


class EditProfileView(UpdateView):
    model = Profile
    form_class = UpdateProfileForm
    template_name = 'my_auth/edit_profile.html'
    slug_field = 'user_id'
    slug_url_kwarg = 'user_id'
    extra_context = {'page_title': 'Редактирование профиля'}

    def get_success_url(self):
        user_id = self.kwargs.get('user_id')
        return reverse('core:profile', args=(self.request.user.id,))

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()  # obj конкретный профиль, кот мы получаем с помощью user_id
        if obj.user != request.user:
            raise Http404('Вы не можете редактировать чужой профиль!')
        return super().dispatch(request, *args, **kwargs)
