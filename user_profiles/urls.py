from django.urls import path

from .views import register, user_login, user_logout, profile_model_detail_view

app_name = 'user_profiles'
urlpatterns = [
    #url(r'^profile/$', profile_model_detail_view, name='profile-detail'),
    #url(r'^(?P<id>\d+)/$', student_profile_detail_view, name='student-detail'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
