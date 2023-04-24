from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
# class AuthUser(models.Model):  # Класс авторизованных пользователей
#     user = models.OneToOneField(User, on_delete=models.CASCADE)


class Category(models.Model):  # Категории объявлений
    name = models.CharField(max_length = 32, unique=True)

    def __str__(self) -> str:
        return self.name


class Announcement(models.Model):  # Объявления
    title = models.CharField(max_length=255)
    description = models.TextField()  #TODO
    cost = models.IntegerField(default=0)
    datetime = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.datetime}' \
        f'{self.title}' \
        f'{self.description}' \
        f'{self.cost}'
    
    def get_absolute_url(self):
        return reverse('announcement_detailed', args=[str(self.id)])


class Answer(models.Model):  # Отклики на объявления
    # text = models.TextField
    datetime = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE)



    
    