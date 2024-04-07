from django.contrib import admin

from .models import Notice, Category, Reply

admin.site.register(Notice)
admin.site.register(Category)
admin.site.register(Reply)
