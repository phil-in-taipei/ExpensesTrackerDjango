from django.contrib.auth import login, get_user_model, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import UserProfile
from .forms import UserProfileForm

User = get_user_model()


@login_required()
def user_profile_create(request):
    current_user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST or None)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.user = current_user
            form_obj.save()
            return HttpResponseRedirect(reverse('user_profiles:profile_detail'))
    else:
        form = UserProfileForm()
    context = {
        "user": current_user,
        "form": form,
    }
    template = "user_profiles/profile-create.html"
    return render(request, template, context)


@login_required()
def user_profile_detail(request):
    current_user = request.user
    user_profile = get_object_or_404(UserProfile, user=current_user)
    context = {
        "user": current_user,
        "user_profile": user_profile,
    }

    template = "user_profiles/profile-detail.html"
    return render(request, template, context)


@login_required()
def user_profile_update(request):
    current_user = request.user
    user_profile = get_object_or_404(UserProfile, user=current_user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST or None, instance=user_profile)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.save()
            return HttpResponseRedirect(reverse('user_profiles:profile_detail'))
    else:
        form = UserProfileForm(instance=user_profile)
    context = {
        "user": current_user,
        "user_profile": user_profile,
        "form": form,
    }

    template = "user_profiles/profile-update.html"
    return render(request, template, context)
