from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'^$', views.UserHome.as_view(), name='userhome'),
    url(r'^login/$', views.SignInView.as_view(), name='signin'),
    url(r'^posts/$', views.UserPosts.as_view(), name='users_posts'),
    url(r'^comments/$', views.UserComments.as_view(), name='users_comments'),
    url(r'^signup/$', views.SignUpView.as_view(), name='signup')
]