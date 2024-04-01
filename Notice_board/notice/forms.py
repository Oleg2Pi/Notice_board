from django import forms
from .models import Notice


class SearchForm(forms.Form):
    query = forms.CharField(label='Поиск', max_length=100)


class NotForm(forms.ModelForm):

    class Meta:
        model = Notice
        fields = ['title', 'text', 'images', 'videos']
