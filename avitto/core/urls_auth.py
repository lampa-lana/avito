from django.urls import path
from .views_auth import MyLoginView, logout_view, EditProfileView, ProfileView, AllProfileView


# app_name = 'core'

urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/<int:user_id>/', ProfileView.as_view(), name='profile'),
    path('profiles/', AllProfileView.as_view(), name='all_profile'),
    path('profile/<int:user_id>/edit/',
         EditProfileView.as_view(), name='edit_profile'),
]
