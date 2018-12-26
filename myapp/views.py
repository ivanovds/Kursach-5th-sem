from django.shortcuts import render, redirect
from .forms import OrderForm

from .models import Order
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html', locals())


def about(request):
    return render(request, 'about.html', locals())


def order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST or None)
        if form.is_valid():
            form.save()

    else:
        form = OrderForm()

    return render(request, 'order.html', {'form': form})





# def order_view(request):
#     if request.method == 'POST':
#         if request.user.is_authenticated:
#             form = OrderForm2(request.POST or None)
#             if form.is_valid():
#                 form.email = 'super@email.com'
#                 form.save()
#         else:
#             form = OrderForm(request.POST or None)
#             if form.is_valid():
#                 form. = 'super@email.com'
#                 form.save()
#     else:
#         if request.user.is_authenticated:
#             form = OrderForm2()
#         else:
#             form = OrderForm()
