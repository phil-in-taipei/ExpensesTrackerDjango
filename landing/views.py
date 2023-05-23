from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from user_profiles.models import UserProfile
from datetime import date


@login_required()
def landing_page(request):
    current_user = request.user
    user_profile = get_object_or_404(UserProfile, user=current_user)
    current_date = date.today()
    context = {
        "user_profile": user_profile,
        "current_date": current_date.strftime("%B %d, %Y")
    }
    template = "landing/landing-page.html"
    return render(request, template, context)
