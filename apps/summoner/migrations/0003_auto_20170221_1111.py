# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-02-21 11:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('summoner', '0002_summoner_region'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='summoner',
            unique_together=set([('summoner_name', 'region')]),
        ),
    ]