from django.db import models
from myapp.models import Course


class Feedback(models.Model):
    customer_name = models.CharField(max_length=120)
    email = models.EmailField()
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    details = models.TextField()
    happy = models.BooleanField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.customer_name
