from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Profile


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('lastname', 'email')


class CustomUserChangeForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'lastname', 'email']
        help_texts = {
            'username': None,
        }


class ProfileChangeForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user', 'firstname', 'lastname', 'email', 'password']
