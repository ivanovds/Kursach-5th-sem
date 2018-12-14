from django.shortcuts import render
from .forms import CustomerForm

def landing(request):
    form = CustomerForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        new_form = form.save()

    return  render(request, 'landing/landing.html', locals())