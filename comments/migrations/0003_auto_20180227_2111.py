# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-27 21:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180227_2111'),
        ('comments', '0002_auto_20180227_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author_id',
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.User', to_field='username'),
        ),
    ]