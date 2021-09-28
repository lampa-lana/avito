from django.conf.urls import url
from django.conf.urls import url

from .views import index, index2

urlpatterns = [
    url('1/', index, name='index'),
    url('2/', index2, name='index2'),
]
