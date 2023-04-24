from django.urls import path
from .views import AnnouncementList, AnnouncementDetailed, CreateNewAnnouncement, ChangeAnnouncement



urlpatterns = [
    path('', AnnouncementList.as_view(), name='announcement_list'),
    path('<int:pk>', AnnouncementDetailed.as_view(), name='announcement_detailed'),
    path('create_new_announcement/', CreateNewAnnouncement.as_view(), name='create_new_announcement'),
    path('<int:pk>/change_announcement/', CreateNewAnnouncement.as_view(), name='change_announcement'),
    path('<int:pk>/answer/', AnnouncementDetailed.as_view(), name='answer')
]