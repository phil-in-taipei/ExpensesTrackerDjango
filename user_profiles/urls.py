from django.urls import path

from .views import profile_model_detail, \
    profile_model_update, \
    profile_model_create

app_name = 'user_profiles'
urlpatterns = [
    path('create-profile/', profile_model_create, name='profile_create'),
    path('edit-profile/', profile_model_update, name='profile_update'),
    path('profile/', profile_model_detail, name='profile_detail'),
]
