# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 16:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140, verbose_name='\u0418\u043c\u044f')),
            ],
            options={
                'ordering': ('-name',),
                'verbose_name': '\u0427\u0430\u0442',
                'verbose_name_plural': '\u0427\u0430\u0442\u044b',
            },
        ),
    ]
