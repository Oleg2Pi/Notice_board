from django import forms

from .models import Notice, Reply


class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'category', 'content']


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']


class SendForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(SendForm, self).__init__(*args, **kwargs)

    content = forms.CharField(required=True, max_length=400, label='Текст')
