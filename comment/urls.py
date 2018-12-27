from django.conf.urls import url

from . import views

app_name = "comment"

urlpatterns = [
    url(r'^feedback/', views.feedback_view, name='feedback_view'),
]
