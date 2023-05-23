from django.urls import path

from .views import landing_page

app_name = 'landing'
urlpatterns = [
    path('welcome/', landing_page, name='landing-page'),

]