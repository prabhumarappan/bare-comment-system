# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-27 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='parent_id',
            field=models.IntegerField(default=0),
        ),
    ]
