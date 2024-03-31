from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name


class Notice(models.Model):
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='notice'
    )

    title = models.CharField(max_length=100)
    text = models.TextField()
    images = models.ImageField(null=True, blank=True)
    videos = models.FileField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self) -> str:
        return self.title


class Responses(models.Model):
    pass
