# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-26 21:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='password',
        ),
        migrations.AddField(
            model_name='users',
            name='last_accessed',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
