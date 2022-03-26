from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm
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

def addresses(request):
	profile = request.user.profile

	context = {
		'profile': profile,
	}

	return render(request, "users/addresses.html", context)