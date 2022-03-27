from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm, CustomUserChangeForm, ProfileChangeForm
from .models import CustomUser, Profile


def signup(request):
	if request.method == "POST":
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('index')
	else:
		form = CustomUserCreationForm()

	context = {
		'form': form,
	}

	return render(request, "registration/signup.html", context=context)


def profile(request):
	profile = request.user.profile

	context = {
		'profile': profile,
	}

	return render(request, "users/profile.html", context)

def edit_profile(request):
	profile = request.user.profile
	user_form = CustomUserChangeForm(instance=request.user)
	profile_form = ProfileChangeForm(instance=profile)

	if request.method == "POST":
		user_form = CustomUserChangeForm(request.POST, instance=request.user)
		profile_form = ProfileChangeForm(request.POST, request.FILES, instance=profile)
		if profile_form.is_valid() and user_form.is_valid():
			user_form.save()
			profile_form.save()
			return redirect('profile')

	context = {
		'user_form': user_form,
		'profile_form': profile_form,
	}

	return render(request, "users/edit_profile.html", context)