from django.urls import path

from .views import user_profile_detail, \
    user_profile_update, \
    user_profile_create

app_name = 'user_profiles'
urlpatterns = [
    path('create-profile/', user_profile_create, name='profile_create'),
    path('edit-profile/', user_profile_update, name='profile_update'),
    path('profile/', user_profile_detail, name='profile_detail'),
]
