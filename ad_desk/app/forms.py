from django import forms
from .models import Announcement, User
from django.core.exceptions import ValidationError
from requests import request
from django.http import HttpRequest


class CreateNewAnnouncementForm(forms.ModelForm):

    class Meta:
        model = Announcement
        fields = [
            'title',    
            'description',
            'cost',
            'category',
            'author'
        ]

    def clean(self) -> dict[str, any]:
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        description = cleaned_data.get('description')
        cost = cleaned_data.get('cost')
        # category = cleaned_data.get('category')

        if len(title) == 0:
            raise ValidationError({'Заголовок не может быть пустым!'})
        elif title is not None and len(title) > 255:
            raise ValidationError({'Превышен допустимый размер заголовка - 255 символов'})
        
        if len(description) == 0:
            raise ValidationError({'Описание объявления не может быть пустым!'})
        
        if len(str(cost)) == 0:
            raise ValidationError({'Необходимо добавить цену!'})
        
        return cleaned_data
        

        
