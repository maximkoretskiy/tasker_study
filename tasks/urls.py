from django.conf.urls import patterns, include, url
from views import *


urlpatterns = patterns('',
    url(r'^$', dash,name='dashboard'),
    url(r'^add$', task_add),
    url(r'^edit/(?P<task_id>\d+)$', task_edit),
    url(r'^delete/(?P<task_id>\d+)$', task_delete),
    url(r'^complete/(?P<task_id>\d+)$', task_status,{'status': True}),
    url(r'^uncomplete/(?P<task_id>\d+)$', task_status,{'status': False}),
)