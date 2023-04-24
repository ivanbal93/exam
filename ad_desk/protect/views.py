from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from app.models import Answer, Announcement, User


# Create your views here.
class IndexView(LoginRequiredMixin, TemplateView):
    model = Answer
    template_name = 'protect/index.html'
    context_object_name = 'answers'

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context['answers_for_user'] = Answer.objects.all().values()
        context['announcements_of_user'] = Announcement.objects.all().values()
        return context
