from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

)
from django.shortcuts import render, redirect

from .forms import UserRegisterForm, MyUserForm


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST or None)
        # my_form = MyUserForm()
        if form.is_valid():
            form.save()

            # my_form.username = form.cleaned_data.get('username')
            # my_form.first_name = form.cleaned_data.get('first_name')
            # my_form.email = form.cleaned_data.get('email')
            # my_form.first_name = form.cleaned_data.get('password1')
            # my_form.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/home')
    else:
        form = UserRegisterForm()
    return render(request, 'signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/home')
