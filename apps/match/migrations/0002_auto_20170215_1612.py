# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-02-15 16:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('match', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='notes',
            field=models.TextField(default='', help_text='Add notes for this match. What went well? How can you improve?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='summoner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='matches', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
