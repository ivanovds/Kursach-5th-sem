from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=12, default = None)
    email = models.EmailField()