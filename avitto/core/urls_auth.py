from django.urls import path, include
from .views_auth import (MyLoginView)


# app_name = 'core'

urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login')
]
