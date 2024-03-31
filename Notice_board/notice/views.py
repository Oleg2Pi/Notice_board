from django.shortcuts import render
from .models import Notice


def notice_list(request):
    notice = Notice.objects.all()
    return render(request, 'notice/not_list.html', {'notice': notice})


def notice_detail(request, not_id):
    notice = Notice.objects.get(id=not_id)
    return render(request, 'notice/not_detail.html', {'notice': notice})
