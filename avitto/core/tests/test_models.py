from datetime import datetime
from datetime import datetime, timedelta
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from core.models import Post, Profile


class TestPostModel(TestCase):
    def setUp(self):
        self.my_user = User.objects.create(
            username='Ivan',
            password='test',
            email='ivan@test.com')

        self. my_post = Post.objects.create(
            author=self.my_user,
            post_name='name',
            description='description',
            price='35',
        )
        self.my_user.save()
        self.my_post.save()
        super().setUp()

    def test_date_edit(self):
        with self.assertRaises(ValidationError):
            self.my_post.date_edit = datetime.now() + timedelta(days=1)
            self.my_post.full_clean()
            self.my_post.save()

    def test_birth_date_with_future_date(self):
        with self.assertRaises(ValidationError):
            self.my_user.profile.birth_date = datetime.now() + timedelta(days=1)
            self.my_user.profile.full_clean()
            self.my_user.profile.save()


class TestProfileModel(TestCase):
    def setUp(self):
        self.my_user = User.objects.create(
            username='Ivan',
            password='test',
            email='ivan@test.com')

    def test_create_profile_with_user(self):
        self.assertIsNotNone(self.my_user.profile, 'Профиль не создан!!!')
