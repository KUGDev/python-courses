from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Riddle(models.Model):
    riddle_text = models.CharField(max_length = 255)
    pub_date = models.DateTimeField('date published')


class Option(models.Model):
    riddle = models.ForeignKey(Riddle, on_delete = models.CASCADE)
    text = models.CharField(max_length = 255)
    correct = models.BooleanField(default = False)

class Message(models.Model):
    chat = models.ForeignKey(
        Riddle,
        verbose_name='Чат под загадкой',
        on_delete=models.CASCADE)
    author = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE)
    message = models.TextField('Сообщение')
    pub_date = models.DateTimeField(
        'Дата сообщения',
        default=timezone.now)

class UserRiddle(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    riddle = models.ForeignKey(
        Riddle,
        on_delete=models.CASCADE
    )
    attempt = models.IntegerField()
    time_spent = models.IntegerField()