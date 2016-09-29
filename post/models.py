# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, verbose_name=u'Автор', related_name='posts')
    date_created = models.DateTimeField(verbose_name=u'Дата публикации', auto_now_add=True)
    title = models.CharField(verbose_name=u'Заголовок', max_length=140)
    text = models.TextField(verbose_name=u'Текст')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Пост'
        verbose_name_plural = u'Посты'
        ordering = ('-date_created', )

    def get_cent_answers_channel_name(self):
        return "post_%d"%self.id