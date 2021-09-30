from django.db import models
from django.contrib.auth.models import User

# Create your models here.


def user_foto_path(instance, filename):
    return 'user_{0}/foto/{1}'.format(instance.user.id, filename)


def user_directory_path(instance, filename):
    return 'user_{0}/posts/{1}'.format(instance.author.id, filename)


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    about = models.TextField(max_length=500)
    foto = models.ImageField(upload_to=user_foto_path)
    birth_date = models.DateField('Date of Birth', null=True, blank=True)

    def __str__(self) -> str:
        return str(self.user.username)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_name = models.CharField(max_length=30)
    description = models.TextField(max_length=1000, blank=True)
    image = models.ImageField(upload_to=user_directory_path)
    date_pub = models.DateTimeField(auto_now_add=True)
    date_edit = models.DateTimeField(auto_now=True)
    price = models.IntegerField()
    category = models.ManyToManyField(User,  related_name='category')

    def __str__(self) -> str:
        return '{}, publication date {}, {}, {}'.format(self.author.username, self.date_pub, self.post_name, self.price)


class Category(models.Model):
    # category = models.ManyToManyField(User, Post, related_name='category_product')
    category_name = models.CharField(max_length=30)
    description = models.TextField(max_length=100, blank=True)

    def __str__(self) -> str:
        return '{}, {}'.format(self.category_name, self.description)
