from django.urls import path

from .views import register, user_login, user_logout, \
    profile_model_detail, profile_model_update, profile_model_create

app_name = 'user_profiles'
urlpatterns = [
    path('profile/', profile_model_detail, name='profile_detail'),
    path('create-profile/', profile_model_create, name='profile_create'),
    path('edit-profile/', profile_model_update, name='profile_update'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
