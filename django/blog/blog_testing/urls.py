from django.conf.urls import include, url

import views


urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^post/(?P<post_id>\d+)/$', views.post_detail, name='post-detail'),
    url(r'^login/$', views.login_, name='login'),
    url(r'^logout/$', views.logout_, name='logout'),
]
