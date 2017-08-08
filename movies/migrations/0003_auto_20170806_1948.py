# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-06 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20170806_1943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='created',
        ),
        migrations.RemoveField(
            model_name='person',
            name='created',
        ),
        migrations.AddField(
            model_name='movie',
            name='secret',
            field=models.CharField(default='There are no secrets', max_length=133),
        ),
        migrations.AddField(
            model_name='person',
            name='secret',
            field=models.CharField(default='There are no secrets', max_length=133),
        ),
    ]