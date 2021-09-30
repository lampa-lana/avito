# Generated by Django 3.2.7 on 2021-09-30 12:26

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(max_length=500)),
                ('foto', models.ImageField(upload_to=core.models.user_foto_path)),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('image', models.ImageField(upload_to=core.models.user_directory_path)),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('date_edit', models.DateTimeField(auto_now=True)),
                ('price', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(related_name='category', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
