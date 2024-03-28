from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=250)
    


class Notice(models.Model):
    pass


class Responses(models.Model):
    pass