from django.db import models
from django.contrib.auth.models import User

class List(models.Model):
    task = models.CharField(max_length=500)
