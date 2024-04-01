from django.shortcuts import render
from .models import Notice
from .forms import SearchForm


def notice_list(request):
    notice = Notice.objects.all()
    return render(request, 'notice/not_list.html', {'notice': notice})


def notice_detail(request, not_id):
    notice = Notice.objects.get(id=not_id)
    return render(request, 'notice/not_detail.html', {'notice': notice})


def search(request):
    notice = Notice.objects.all()
    form = SearchForm(request.GET)

    if form.is_valid():
        query = form.cleaned_data['query']
        notice = notice.filter(title__icontains=query)

    return render(request, 'notice/search.html', {'form': form, 'notice': notice})
