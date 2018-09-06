from django.db import models
from django.utils import timezone


class Day(models.Model):
    title = models.CharField('タイトル', max_length = 200)
    text = models.TextField('本文')
    date = models.DateTimeField('日付', default = timezone.now)
    user = models.CharField('投稿者', max_length = 20)

    def __str__(self):
        return self.title