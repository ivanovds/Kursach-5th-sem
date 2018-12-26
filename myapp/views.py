from django.shortcuts import render, redirect
from .forms import OrderForm, OrderForm2

from .models import Order
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html', locals())


def about(request):
    return render(request, 'about.html', locals())


def order_view(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = OrderForm2(request.POST or None)
            if form.is_valid():
                form.save()
        else:
            form = OrderForm(request.POST or None)
            if form.is_valid():
                form.save()
    else:
        if request.user.is_authenticated:
            print('YEEEEES')
            form = OrderForm2()
        else:
            form = OrderForm()

    return render(request, 'order.html', {'form': form})

