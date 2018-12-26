from django.db import models
# from django.contrib.auth.models import User


class MyUser(models.Model):
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, default="")
    password = models.CharField(max_length=100)


