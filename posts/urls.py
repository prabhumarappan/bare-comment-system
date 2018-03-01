from django.conf.urls import url
from posts import views

urlpatterns = [
    url(r'^all/$', views.AllPosts.as_view(), name='posts'),
    url(r'^(?P<postid>\d+)/$', views.SinglePost.as_view(), name='singlepost'),
    url(r'^delete/(?P<postid>\d+)/$', views.DeletePost.as_view(), name ='delete'),
    url(r'^add/$', views.AddPost.as_view(), name='addpost')

]