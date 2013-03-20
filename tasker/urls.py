from django.conf.urls import patterns, include, url
from users.views import login_or_redirect

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tasker.views.home', name='home'),
    # url(r'^tasker/', include('tasker.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url( r'^',include('tasks.urls')),
    url( r'^login/$', login_or_redirect ),
    url( r'^logout/$', 'django.contrib.auth.views.logout_then_login' ),
)
