from django_filters import FilterSet, ModelChoiceFilter

from board.models import Reply, Notice


class NoticeFilter(FilterSet):
    notice = ModelChoiceFilter(
        empty_label='Все обьявления',
        field_name='post',
        label='Фильтр по обновлениям',
        queryset=Reply.objects.all()
    )

    class Meta:
        model = Reply
        fields = ('notice',)

    def __init__(self, *args, **kwargs):
        super(NoticeFilter, self).__init__(*args, **kwargs)
        self.filters['notice'].queryset = Notice.objects.filter(notice_author_id=kwargs['request'])
