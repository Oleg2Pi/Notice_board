from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Notice(models.Model):
    notice_author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.title


class Reply(models.Model):
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE, related_name='replies')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    is_allowed = models.BooleanField(default=False)

    def __str__(self):
        return self.author.username + ', ' + self.notice.title

