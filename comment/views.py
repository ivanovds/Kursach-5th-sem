from django.shortcuts import render

from .forms import FeedbackForm


def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST or None)

        if form.is_valid():
            form.save()
            return render(request, 'index.html')
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form.html', {'form': form})
