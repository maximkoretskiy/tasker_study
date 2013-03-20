from django.conf.urls import patterns, include, url
from views import *


urlpatterns = patterns('',
    url(r'^$', dash,name='dashboard'),
    url(r'^add$', task_add),
    url(r'^delete/(?P<task_id>\d+)$', task_delete)
)