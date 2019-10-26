# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-10-26 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='content',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='design',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='usability',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='vote_submissions',
            field=models.IntegerField(default=0),
        ),
    ]