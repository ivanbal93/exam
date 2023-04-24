# Generated by Django 4.2 on 2023-04-08 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_announcement_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='announcement',
            name='description',
            field=models.TextField(default='description'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('ta', 'Танки'), ('he', 'Хилы'), ('dd', 'ДД'), ('de', 'Торговцы'), ('gm', 'Гилдмастеры'), ('qg', 'Квестгиверы'), ('sm', 'Кузнецы'), ('tn', 'Кожевники'), ('pm', 'Зельевары'), ('sm', 'Мастера заклинаний')], default='', max_length=2),
        ),
    ]
