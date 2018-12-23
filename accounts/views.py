from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

)
from django.shortcuts import render
from accounts.forms import UserLoginForm


def login_view(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        new_form = form.save()

    return render(request, "form.html", {"form": form, "title": title})


def register_view(request):
    return render(request, "form.html", {})


def logout_view(request):
    return render(request, "form.html", {})
