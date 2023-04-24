from datetime import datetime

from django.shortcuts import render
from .models import Announcement, Category, Answer
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView
from .filters import AnnouncementFilter
from .forms import CreateNewAnnouncementForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.core.mail import send_mail

# Create your views here.

class AnnouncementList(ListView):
    model = Announcement
    ordering = '-datetime'
    template_name = 'announcement_list.html'
    context_object_name = 'announcement_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = AnnouncementFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filterset'] = self.filterset
        return context


class AnnouncementDetailed(DetailView):
    model = Announcement
    template_name = 'announcement_detailed.html'
    context_object_name = 'announcement_detailed'

    def post(self, request, pk):
        ann = Announcement.objects.get(id=pk)
        ans = Answer()
        ans.announcement_id = pk
        ans.author_id = request.user.id
        ans.save()

        send_mail(
            subject=f'Новый отклик!',
            message=f'Вы получили отклик по объявлению {ann.title}',
            from_email=None,
            recipient_list=[ann.author.email]
        )

        return redirect(request.META.get('HTTP_REFERER'))


class CreateNewAnnouncement(LoginRequiredMixin, CreateView):
    form_class = CreateNewAnnouncementForm
    model = Announcement
    template_name = 'create_new_announcement.html'
    context_object_name = 'create_new_announcement'


class ChangeAnnouncement(LoginRequiredMixin, CreateView):
    form_class = CreateNewAnnouncementForm
    model = Announcement
    template_name = 'create_new_announcement.html'
    context_object_name = 'change_announcement'