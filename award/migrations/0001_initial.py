# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-25 14:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', tinymce.models.HTMLField()),
                ('profile_photo', models.ImageField(null=True, upload_to='photos/')),
                ('contact', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('project_image', models.ImageField(blank=True, upload_to='images/')),
                ('description', models.CharField(max_length=30)),
                ('link', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='user_project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='award.Project'),
        ),
    ]
