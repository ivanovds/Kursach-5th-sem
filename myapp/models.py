from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    customer_name = models.CharField(max_length=150)
    # customer_name = models.ForeignKey(User, related_name='first_name', on_delete=models.SET_NULL, null=True)
    telephone = models.CharField(max_length=13)
    email = models.EmailField(max_length=50, default="")
    username = models.CharField(max_length=150, default="")

    def __str__(self):
        return self.course
