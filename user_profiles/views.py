from django.contrib.auth import login, get_user_model, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import RegisterForm, UserLoginForm, UpdateProfile

User = get_user_model()


@login_required(redirect_field_name='login')
def profile_model_create(request):
    current_user = request.user
    user_profile = get_object_or_404(UserProfile, user=current_user)
    if request.method == 'POST':
        form = UpdateProfile(request.POST or None, instance=user_profile)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.save()
            return HttpResponseRedirect('/user-profiles/profile')
    else:
        form = UpdateProfile()
    context = {
        "user": current_user,
        "user_profile": user_profile,
        "form": form,
    }
    template = "user_profiles/profile-create-view.html"
    return render(request, template, context)


@login_required(redirect_field_name='login')
def profile_model_detail(request):
    current_user = request.user
    user_profile = get_object_or_404(UserProfile, user=current_user)
    context = {
        "user": current_user,
        "user_profile": user_profile,
    }

    template = "user_profiles/profile-detail-view.html"
    return render(request, template, context)


@login_required(redirect_field_name='login')
def profile_model_update(request):
    current_user = request.user
    user_profile = get_object_or_404(UserProfile, user=current_user)
    if request.method == 'POST':
        form = UpdateProfile(request.POST or None, instance=user_profile)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.save()
            return HttpResponseRedirect('/user-profiles/profile')
    else:
        form = UpdateProfile(instance=user_profile)
    context = {
        "user": current_user,
        "user_profile": user_profile,
        "form": form,
    }

    template = "user_profiles/profile-update-view.html"
    return render(request, template, context)


def register(request, *args, **kwargs):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/user-profiles/login")
    return render(request, "user_profiles/register.html", {"form": form})


def user_login(request, *args, **kwargs):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username_ = form.cleaned_data.get('username')
        user_obj = User.objects.get(username__iexact=username_)
        login(request, user_obj) # landing-page/welcome-page/
        user_profile = UserProfile.objects.filter(user=user_obj).first()
        if user_profile.email and user_profile.surname \
                and user_profile.given_name and user_profile.age:
            return HttpResponseRedirect("/") # redirect to a landing page
        else:
            return HttpResponseRedirect("/user-profiles/create-profile") # redirect to a landing page
    return render(request, "user_profiles/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/user-profiles/login")
