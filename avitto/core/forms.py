from django import forms
from django.core.exceptions import ValidationError
from django.forms import fields
from .models import Post


class PostForm(forms.ModelForm):
    max_size_img = 5

    class Meta:
        model = Post
        fields = ['post_name', 'description',
                  'image', 'date_pub', 'price', 'category']
        widgets = {
            'post_name': forms.TextInput(attrs={'class': 'post-title', 'placeholder': 'Продам что-нибудь'}),
            'description': forms.Textarea(attrs={'class': 'post-text', 'placeholder': 'Подробнее, о том что продаю'}),
            'image': forms.ClearableFileInput(attrs={'class': 'post-image', }),
            # 'date_pub': forms.SplitDateTimeWidget(attrs={'class': 'post-image', }),
            'price': forms.NumberInput(attrs={'class': 'post-price', }),

        }

    def clean_post_name(self):
        post_name = self.cleaned_data.get('post_name')
        if len(post_name) < 6:
            raise ValidationError('Наименование слишком короткое!')
        else:
            return post_name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 6:
            raise ValidationError('Описание товара слишком короткое!')
        else:
            return description

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > self.max_size_img*1024*1024:
                raise ValidationError(
                    'Файл должен быть не больше {} мб'.format(self.max_size_img))
            return image
        else:
            raise ValidationError('Не удалось прочитать файл')
