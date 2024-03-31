from django.urls import path
from .views import notice_detail, notice_list


urlpatterns = [
    path('', notice_list, name='not_list'),
    path('<int:not_id>/', notice_detail, name='not_detail'),
]
