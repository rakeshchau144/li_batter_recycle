from django.db import models

# Create your models here.
class Employee(models.Model):
    Email = models.CharField(max_length=100)
    paass = models.CharField(max_length=100)