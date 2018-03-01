# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from django.shortcuts import redirect
from users.models import User
from posts.models import Post
from comments.models import Comment
from django.http import HttpResponseForbidden

class SignInView(TemplateView):
    def get(self, request):
        if 'username' not in request.session:
            return render(request, 'login.html', context=None)
        else:
            response = redirect('/users/')
            return response

    def post(self, request):
        username = request.POST['name']
        existing = User.objects.filter(username=username)
        if not existing:
            return render(request, 'login.html', {'error': "User does not exist, create a new one by signing up!"})
        else:
            user = existing.first()
            userid = user.pk
            response = redirect('/users/')
            request.session['username'] = username
            request.session['userid'] = userid
            return response


class SignUpView(TemplateView):
    def get(self, request):
        return render(request, 'signup.html', context=None)

    def post(self, request):
        username = request.POST['name']
        existing = User.objects.filter(username=username)
        if not existing:
            new_user = User(username=username)
            new_user.save()
            if new_user:
                return render(request, 'signup.html', {'message': "Created successfully! Go to login page"})
            else:
                return render(request, 'signup.html', {'error': "Nope!"})
        else:
            return render(request, 'signup.html', {'error': "Already Exists! Enter a unique one."})


class UserPosts(TemplateView):
    def get(self, request):
        if 'username' in request.session:
            userid = request.session['userid']
            user_posts = Post.objects.filter(author_id=userid).order_by('-created')
            return render(request, 'user-posts.html', {'posts': user_posts})
        else:
            return HttpResponseForbidden("Unauthorized Access. <a href='/users/login/'>Login</a>")


class UserComments(TemplateView):
    def get(self, request):
        if 'username' in request.session:
            userid = request.session['userid']
            user_comments = Comment.objects.filter(author_id=userid).order_by('-created')
            for comments in user_comments:
                print comments.post_id
            return render(request, 'user-comments.html', {'comments': user_comments})
        else:
            return HttpResponseForbidden("Unauthorized Access. <a href='/users/login/'>Login</a>")


class UserHome(TemplateView):
    def get(self, request):
        if 'username' in request.session:
            return render(request, 'userhome.html')
        else:
            response = redirect('/users/login')
            return response