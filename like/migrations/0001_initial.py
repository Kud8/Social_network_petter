# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 16:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dislikes', models.ManyToManyField(related_name='dislike', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(related_name='like', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
