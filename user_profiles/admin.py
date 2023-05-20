from django.contrib import admin

from .models import UserProfile

admin.site.site_header = 'Expenses Tracker'

admin.site.register(UserProfile)
