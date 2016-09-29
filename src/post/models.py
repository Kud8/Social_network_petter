from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'Автор', related_name='posts')
    date_created = models.DateTimeField(verbose_name=u'Дата публикации', auto_now_add=True)
    title = models.CharField(verbose_name=u'Заголовок', max_length=140)
    text = models.TextField(verbose_name=u'Текст')
    location = models.PointField(verbose_name='Место публикации')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Пост'
        verbose_name_plural = u'Посты'
        ordering = ('-pub_date', )

    def get_cent_answers_channel_name(self):
        return "post_%d"%self.id