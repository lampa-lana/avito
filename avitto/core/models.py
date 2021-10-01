from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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


class Category(models.Model):
    category_name = models.CharField(max_length=30)
    description = models.TextField(max_length=1000, blank=True)

    def __str__(self) -> str:
        return '{}, {}'.format(self.category_name, self.description)


class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    post_name = models.CharField(max_length=30)
    description = models.TextField(max_length=1000, blank=True)
    image = models.ImageField(upload_to=user_directory_path)
    date_pub = models.DateTimeField(default=timezone.now)
    date_edit = models.DateTimeField(default=timezone.now)
    price = models.IntegerField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True,  related_name='category')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self) -> str:
        return '{}, publication date {}, {}, {}, category{}'.format(self.author.username, self.date_pub, self.post_name, self.price, self.category)
