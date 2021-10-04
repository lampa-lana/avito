from django.contrib import admin
from .models import Profile, Post, Category

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'foto', 'birth_date')
    list_display_links = ('user', 'id',)
    search_fields = ('id', 'birth_date')


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'post_name', 'date_pub', 'price', 'category')
    list_display_links = ('author', 'post_name', 'category')
    search_fields = ('post_name', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'description')
    list_display_links = ('category_name',)
    search_fields = ('category_name',)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
