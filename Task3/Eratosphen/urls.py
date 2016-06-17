from django.conf.urls import patterns, url
from Eratosphen import views

urlpatterns = patterns('',
                       url(r'^d+/$', views.simple_num, name='simple_num'),
                       )
