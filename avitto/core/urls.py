from django.conf.urls import url
from django.conf.urls import url
from django.urls import path, include
from .views import index, index2

urlpatterns = [
    url('1/', index, name='index'),
    path('2/', index2, name='index2'),
]
