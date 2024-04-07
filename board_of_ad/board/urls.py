from django.urls import path

from .views import NoticeList, NoticeDetail, NoticeCreate, ReplyAdd, NoticeEdit, Replies, delete_reply, delete_notice, \
   allow_reply, news_send

urlpatterns = [
   path('', NoticeList.as_view(), name='notice_list'),
   path('<int:pk>', NoticeDetail.as_view(), name='notice'),
   path('create/', NoticeCreate.as_view(), name='noticecreate'),
   path('<int:pk>/reply/add', ReplyAdd.as_view(), name='reply_add'),
   path('<int:pk>/edit', NoticeEdit.as_view(), name='notice_edit'),
   path('replies/', Replies.as_view(), name='replies'),
   path('delete/<int:pk>', delete_reply, name='delete_reply'),
   path('<int:pk>/delete', delete_notice, name='delete_notice'),
   path('<int:pk>/allow', allow_reply, name='allow_reply'),
   path('send_mails/', news_send, name='send_mails'),
]
