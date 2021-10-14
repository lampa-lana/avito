from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls.base import reverse
from .forms_auth import LoginForm


class MyLoginView(LoginView):
    template_name = 'my_auth/login.html'
    form = LoginForm

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
