from django.urls import path
from .views import (
    notice_detail, notice_list, search, created_not
)


urlpatterns = [
    path('', notice_list, name='not_list'),
    path('<int:not_id>/', notice_detail, name='not_detail'),
    path('search/', search, name='search'),
    path('created_not/', created_not, name='created_not'),
]
