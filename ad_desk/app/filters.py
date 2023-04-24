from django_filters import ModelChoiceFilter, FilterSet
from .models import Announcement, Category


class AnnouncementFilter(FilterSet):
    category = ModelChoiceFilter(
        field_name = 'category',
        queryset = Category.objects.all(),
        label = 'Категория',
        empty_label = ''
    )