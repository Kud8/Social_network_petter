# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Message(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'Автор', related_name='messages')
    date_created = models.DateTimeField(verbose_name=u'Время отправления', auto_now_add=True)
    text = models.TextField(verbose_name=u'Текст')
    chat = models.ForeignKey('chat.Chat', verbose_name=u'Чат', related_name='messages')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Сообщение'
        verbose_name_plural = u'Сообщения'
        ordering = ('-date_created', )
