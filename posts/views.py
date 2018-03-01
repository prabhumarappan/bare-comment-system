# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import ast
from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseForbidden
from django.http import HttpResponse
from posts.models import Post
from users.models import User
from comments.models import Comment
import time

class AllPosts(TemplateView):
    def get(self, request):
        try:
            username = request.session['username']
            if username is not None:
                posts = Post.objects.all()
                return render(request, 'posts.html', {'posts': posts})
        except Exception as e:
            print e
            return HttpResponseForbidden("Unauthorized Access. <a href='/users/login/'>Login</a>")


class SinglePost(TemplateView):
    def get(self, request, postid):
        try:
            post = Post.objects.filter(pk=postid)
            comments = Comment.objects.filter(post_id=post).order_by('parent_id', 'created')
            comments = comments.values()
            current_user = request.session['username']
            comments_result = [x for x in comments]
            post_result = [x for x in post]
            
            for comment in comments_result:
                comment['created'] = int(time.mktime(comment['created'].timetuple()))
                comment['author'] = User.objects.get(pk=comment['author_id']).username;
            comments_string = json.dumps(comments_result)
            return render(request, 'singlepost.html', {'post': post, 'comments': comments_string, 'user': current_user})
        except Exception as e:
            print e
            return HttpResponseForbidden("Unauthorized Access. <a href='/users/login/'>Login</a>")

    def post(self, request, postid):
        comment = request.POST['comment']
        author_id = request.session['userid']
        parent_id = request.POST['parent_id']

        post = Post.objects.get(pk=postid)
        author = User.objects.get(pk=author_id)
        
        new_comment = Comment(message=comment,post_id=post,author=author,parent_id=parent_id)
        new_comment.save()

        return_message = {"success":200}
        return HttpResponse(json.dumps(return_message), content_type='application/json')


class DeletePost(TemplateView):
    def post(self, request, postid):
        comment_id = request.POST['comment_id']

        Comment.objects.filter(pk=comment_id).delete()

        return_message = {"success":200}
        return HttpResponse(json.dumps(return_message), content_type='application/json')


class AddPost(TemplateView):
    def get(self, request):
        try:
            username = request.session['username']
            return render(request, 'addpost.html', context=None)
        except Exception as e:
            print e
            return HttpResponseForbidden("Unauthorized Access. <a href='/users/login/'>Login</a>")
    

    def post(self, request):
        try:
            username = request.session['username']
            userid = request.session['userid']
            posttitle = request.POST['posttitle']
            user = User.objects.get(pk=userid)
            new_post = Post(title=posttitle,author=user)
            new_post.save()
            return_message = {"success":200}
            return HttpResponse(json.dumps(return_message), content_type='application/json')
        except Exception as e:
            print e
            return HttpResponseForbidden("Unauthorized Access. <a href='/users/login/'>Login</a>")