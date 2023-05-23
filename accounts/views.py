from django.contrib.auth import login, get_user_model, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render

from user_profiles.models import UserProfile
from .forms import UserLoginForm, RegisterForm

User = get_user_model()


def register(request, *args, **kwargs):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/accounts/login")
    return render(request, "accounts/register.html", {"form": form})


def user_login(request, *args, **kwargs):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username_ = form.cleaned_data.get('username')
        user_obj = User.objects.get(username__iexact=username_)
        login(request, user_obj) # landing-page/welcome-page/
        user_profile = UserProfile.objects.filter(user=user_obj).first()
        if user_profile:
            return HttpResponseRedirect("/") # redirect to a landing page
        else:
            return HttpResponseRedirect("/user-profiles/create-profile") # redirect to a landing page
    return render(request, "accounts/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/accounts/login")
