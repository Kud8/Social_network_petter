# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Like(models.Model):
    likes = models.ManyToManyField(User, related_name='like')
    dislikes = models.ManyToManyField(User, related_name='dislike')

    def rate(self):
        return self.likes.count() - self.dislikes.count()

    class Meta:
        verbose_name = u'Лайк'
        verbose_name_plural = u'Лайки'