# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from posts.models import Post
from users.models import User


class Comment(models.Model):
    message = models.CharField(max_length=700)
    post_id = models.ForeignKey(Post, to_field='id', default=1)
    author = models.ForeignKey(User, to_field='id', default=1)
    created = models.DateTimeField(auto_now_add=True)
    parent_id = models.IntegerField(default=0)

    def __unicode__(self):
        return self.message
    #
    # class Meta:
    #     ordering = ['parent_id', '-created']