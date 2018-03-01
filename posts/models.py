# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from users.models import User


class Post(models.Model):
    title = models.CharField(max_length=500)
    author = models.ForeignKey(User, to_field='id', default=1)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title
