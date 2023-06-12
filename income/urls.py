from django.urls import path

from .views import create_income_source, \
    update_income_source, user_income_sources

app_name = 'income'
urlpatterns = [
    path('create-income-source/', create_income_source, name='create_income_source'),
    path('update-income-source/<int:id>/', update_income_source, name='update_income_source'),
    path('user-income-sources/', user_income_sources, name='user_income_sources'),
]
