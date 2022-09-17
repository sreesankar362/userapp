from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import View, FormView, CreateView, UpdateView

from posts.forms import PostForm
from .forms import UserRegistrationForm, LogInForm, ProfileForm
from django. contrib import messages
from .models import Profile
from django.contrib.auth.models import User
from django.http import JsonResponse


class RegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = "register.html"
    model = User
    success_url = reverse_lazy("login")

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            form = UserRegistrationForm(request.POST)
            messages.error(request, "Invalid Entry")
            return render(request, self.template_name, {"form" : form})


class LogInView(FormView):
    form_class = LogInForm
    template_name = 'login.html'
    model = User

    def post(self, request, *args, **kwargs):
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("home")


            else:
                form = LogInForm(request.POST)
                messages.error(request, "Invalid Credentials")
                return render(request, "login.html", {"form": form})
        else:
            form = LogInForm(request.POST)
            return render(request, "login.html", {"form": form})


def logoutfn(request, *args, **kwargs):
    logout(request)
    return redirect("login")


class ProfileView(CreateView):
    form_class = ProfileForm
    model = Profile
    template_name = "profile.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        self.object = form.save()
        messages.success(self.request, "Profile Added Successfully!")
        return super().form_valid(form)


class UpdateProfileView(UpdateView):
    form_class = ProfileForm
    model = Profile
    template_name = "updateprofile.html"
    success_url = reverse_lazy("home")
    pk_url_kwarg = 'user_id'

    def form_valid(self, form):
        messages.success(self.request, "Profile Updated Successfully")
        self.object = form.save()
        return super().form_valid(form)


