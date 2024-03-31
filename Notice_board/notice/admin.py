from django.contrib import admin
from .models import Person, Notice


admin.site.register(Person)
admin.site.register(Notice)