from django_filters import FilterSet  # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import *
import django_filters

#
# class CommentFilter(FilterSet):
#     class Meta:
#         model = Comment
#         filter_fields = ["commentPost"]


class CommentFilter(FilterSet):
    comments = django_filters.CharFilter(field_name='commentPost', lookup_expr='icontains',
                                            label='Пост')