
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'placeholder':'create password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'placeholder':'confirm password'}),
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2"

        ]
        widgets = {
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"})

        }


class LogInForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
        widgets = {

            "date_of_birth": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "bio": forms.TextInput(attrs={"class": "form-control"}),
            "phone_number": forms.NumberInput(attrs={"class": "form-control"}),
            "profile_pic": forms.FileInput(attrs={"class": "form-control"}),
            "gender": forms.TextInput(attrs={"class": "form-control"})
        }