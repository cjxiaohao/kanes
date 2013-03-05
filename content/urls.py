from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^_/$', 'content.views.all', name='content_all' ),
    url(r'_/write/(?P<path>[\w\/]+)?$', 'content.views.write', name='content_write'),
    url(r'^(?P<user>[\w\d]+)\/(?P<path>[\w\d]+)?$', 'content.views.view', \
        name='content_view'),
)
