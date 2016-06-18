from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^list/(?P<id>\d+)/$', views.simple_num, name='simple_num'),
    url(r'^$', views.index, name='index'),
]
